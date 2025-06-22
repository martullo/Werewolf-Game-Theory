from claim import Claim
import random

import copy
class RandomStrategy:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self, id):
        self.role = 'seer'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.roles = None  # Roles of players, to be set by the game manager
        self.claims = None
        self.checked_players = dict()

    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)

    def vote(self):
        return None  

    def claimRoles(self):
        claim = Claim(self.players)
        # for player in self.players:
        #     if player == self.id:
        #         claim.make_claim(player, 'seer')
        #     else:
        #         claim.make_claim(player, random.choice(['villager', 'werewolf', 'witch']))
        claim.make_claim(self.id, 'seer')  # Claiming self as seer
        
        return claim
        # return Claim(self.players)


    def reveal(self):
        return True

    def choosePlayerToCheck(self):
        return random.choice(self.players)

    def updateRoleClaimsAfterSeen(self, player: int, role: str):
        self.checked_players[player] = role
    
    def lastWord(self):
        claim = self.claimRoles()
        return claim



class RandomStrategyAdvanced:
    """
    Random strategy implementation.
    Seer doesn't check herself, doesn't check same player more then once
    """
    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()
    
    def __init__(self, id):
        self.role = 'seer'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.belief_table = None  # Belief table, to be set by the game manager

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)

    def vote(self):
        return None  

    def claimRoles(self, id, claim, players, checked_players, is_revealed=False):
        for player in players:
            if player == id:
                if is_revealed:
                    claim.make_claim(player,self.role)
                else:
                    claim.make_claim(player, 'villager')
            elif player in checked_players.keys():
                claim.make_claim(player, checked_players.get(player, None))
            else:
                claim.make_claim(player, random.choice(['villager']))
            
        return claim

    def reveal(self):
        return True
    
    def choosePlayerToCheck(self):
        to_check = copy.deepcopy(self.players)
        to_check.remove(id)
        for p in self.checked_players.keys():
            if p in to_check:
                to_check.remove(p) #no double checking
        return random.choice(to_check)

    def lastWord(self):
        return Claim(self.players)