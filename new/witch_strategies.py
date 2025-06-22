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
        self.belief_table = None  # Belief table, to be set by the game manager
        self.roles = None  # Roles of players, to be set by the game manager

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return random.choice(self.players + ['skip'])

    def claimRoles(self):
        claim = Claim(self.players)
        for player in self.players:
            existing_roles = [role for role in ['villager', 'werewolf', 'seer', 'witch'] if self.roles[role] > 0]
            claim.make_claim(player, random.choice(existing_roles))
        return claim
        
    def decideSaveOrPoison(self, player):
        return random.choice([player] + [random.choice(self.players)])
    
    def open_up(self):
        pass
    def lastWord(self):
        return self.claimRoles()
# TODO: Implement optimal strategy for witches

class OptimalStrategy:
    def __str__(self):
        return f"{self.role} (id {self.id})"

    def __repr__(self):
        return self.__str__()

    def __init__(self, id):
        self.role = 'witch'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.belief_table = None  # Belief table, to be set by the game manager
        self.roles = None  # Roles of players, to be set by the game manager
        self.day = 1

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return random.choice(self.players + ['skip'])

    def claimRoles(self):            
        return claim
        
    def decideSaveOrPoison(self, player):
        return random.choice([player] + [random.choice(self.players)])
    
    def open_up(self):
        pass
    def lastWord(self):
        return self.claimRoles()
