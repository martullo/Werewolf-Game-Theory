from claim import Claim
import random

class RandomStrategy:
    def __str__(self):
        return f"{self.role} (id {self.id})"

    def __repr__(self):
        return self.__str__()

    def __init__(self, id):
        self.role = 'witch'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.roles = None  # Roles of players, to be set by the game manager
        self.claims = None
        self.used_potions = {'save': False, 'poison': False}

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'seer' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)

    def vote(self):
        werewolves = []
        for player in self.players:
            self.claims.get_claim(player)
            if self.claims.get_claim(player) == 'werewolf':
                werewolves.append(player)
        if werewolves:
            return random.choice(werewolves)
        return random.choice(self.players + ['skip'])
    
    def claimRoles(self):
        return self.claims

    def decideSaveOrPoison(self, player):
        self.claims.make_claim(self.id, 'witch')
        if self.used_potions['save'] and self.used_potions['poison']:
            return None
        if not self.used_potions['save'] and not self.used_potions['poison']:
            ability = random.choice(['save', 'poison'])
        elif not self.used_potions['save']:
            ability = 'save'
        else:
            ability = 'poison'
        if ability == 'save':
            self.used_potions['save'] = True
            self.claims.make_claim(player, 'villager')
            return player
        else:
            self.used_potions['poison'] = True
            poisoned_player = self.vote()
            while poisoned_player == player:
                poisoned_player = self.vote()
            return poisoned_player
    
    def lastWord(self):
        return self.claimRoles()

class SilentStrategy:
    """
    Don't open up until killed.
    """
    def __str__(self):
        return f"{self.role} (id {self.id})"

    def __repr__(self):
        return self.__str__()

    def __init__(self, id):
        self.role = 'witch'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.roles = None  # Roles of players, to be set by the game manager
        self.claims = None
        self.used_potions = {'save': False, 'poison': False}
        self.saved_player = None

    def reactToDeath(self, last_words):
        self.reactToClaims([last_words])

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'seer' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)

    # Vote for random werewolf if claims exist, otherwise vote random player or skip
    def vote(self):
        werewolves = []
        for player in self.players:
            self.claims.get_claim(player)
            if self.claims.get_claim(player) == 'werewolf':
                werewolves.append(player)
        if werewolves:
            return random.choice(werewolves)
        return random.choice(self.players + ['skip'])


    def claimRoles(self):
        return Claim(self.players)

    # Randomly decide to save or poison a player, when poison use claims for werewolves (just like vote)
    def decideSaveOrPoison(self, player):
        if self.used_potions['save'] and self.used_potions['poison']:
            return None
        if not self.used_potions['save'] and not self.used_potions['poison']:
            ability = random.choice(['save', 'poison'])
        elif not self.used_potions['save']:
            ability = 'save'
        else:
            ability = 'poison'
        if ability == 'save':
            self.used_potions['save'] = True
            return player
        else:
            self.used_potions['poison'] = True
            poisoned_player = self.vote()
            while poisoned_player == player:
                poisoned_player = self.vote()
            return poisoned_player

    def lastWord(self):
        if self.saved_player:
            self.claims.make_claim(self.saved_player, 'villager')
        else:
            self.claims.make_claim(self.id, 'witch')
        return self.claims