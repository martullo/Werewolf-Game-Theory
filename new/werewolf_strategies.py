from claim import Claim
import random


class RandomStrategy:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """
    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()
    
    def __init__(self, id):
        self.role = 'werewolf'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.werewolves = []  # List of werewolf teammates, to be set by the game manager
        self.roles = None  # Roles of players, to be set by the game manager
        self.claims = None

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'seer' in plainClaim.values() or 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)
    
    def vote(self):
        players = [p for p in self.players if p not in self.werewolves]
        return random.choice(self.players + ['skip'])
    
    def claimRoles(self):
        return Claim(self.players)
    
    def chooseVictim(self):
        players = [p for p in self.players if p not in self.werewolves]
        return random.choice(players) #no friendly fire at night
    
    def lastWord(self):
        claim = self.claimRoles()
        return [claim]

class RandomStrategyNoFriendlyFire:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """
    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()
    
    def __init__(self, id):
        self.role = 'werewolf'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.werewolves = []  # List of werewolf teammates, to be set by the game manager
        self.roles = None  # Roles of players, to be set by the game manager
        self.claims = None

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'seer' in plainClaim.values() or 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)
    
    def vote(self):
        return self.chooseVictim() #no friendly fire at all
    
    def claimRoles(self):
        return Claim(self.players)
    
    def chooseVictim(self):
        players = [p for p in self.players if p not in self.werewolves]
        return random.choice(players)
    
    def lastWord(self):
        claim = self.claimRoles()
        return [claim]
    

class BeastStrategy:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """
    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()
    
    def __init__(self, id):
        self.role = 'werewolf'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.werewolves = []  # List of werewolf teammates, to be set by the game manager
        self.roles = None  # Roles of players, to be set by the game manager
        self.claims = None

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'seer' in plainClaim.values() or 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)
    
    def vote(self):
        return self.chooseVictim() #no friendly fire at all
    
    def claimRoles(self):
        return Claim(self.players)
    
    def chooseVictim(self):

        players = [p for p in self.players if p not in self.werewolves] #no friendly fire
        claims = self.claims.claims
        if 'seer' in claims.values():
            for player, role in claims.items():
                if role == 'seer' and player in self.players:
                    return player
                
        if 'witch' in claims.values():
            for player, role in claims.items():
                if role == 'witch' and player in self.players:
                    return player
                
        if 'villager' in claims.values():
            for player, role in claims.items():
                if role == 'villager' and player in self.players:
                    return player

        
                
        return random.choice(players)
    
    def lastWord(self):
        claim = self.claimRoles()
        return [claim]
    