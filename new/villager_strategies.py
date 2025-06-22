from claim import Claim
import random
import copy
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
        self.role = 'villager'
        self.players:list[int] = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.claims = None

    def reactToDeath(self, last_words):
        self.reactToClaims(last_words)

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'seer' in plainClaim.values() or 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)
        
        


    def vote(self):
        return random.choice(self.players + ['skip'])
    
    def claimRoles(self):
        return Claim(self.players)

    def lastWord(self):
        claim = self.claimRoles()
        return [claim]
    

class TrustStrategy:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """
    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()
    
    def __init__(self, id):
        self.role = 'villager'
        self.players:list[int] = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.claims = None

    def reactToDeath(self, last_words):
        self.reactToClaims(last_words)

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'seer' in plainClaim.values() or 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)
        
        


    def vote(self):
        forbidden = []
        claims = self.claims.claims
        if 'werewolf' in claims.values():
            for id, role in claims.items():
                if role == 'werewolf' and id in self.players:
                    return id
        for id, role in claims.items():
            if role == 'seer' or role == 'witch' or role == 'villager':
                forbidden.append(id)
        to_vote = copy.deepcopy(self.players)
        to_vote.remove(self.id)
        for p in forbidden:
            if p in to_vote:
                to_vote.remove(p) 
        return random.choice(to_vote + ['skip'])

            

    
    def claimRoles(self):
        return self.claims#Claim(self.players)

    def lastWord(self):
        claim = self.claimRoles()
        return [claim]
    














class OptimalStrategy:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self, id):
        self.role = 'villager'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.belief_table = None  # Belief table, to be set by the game manager

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return random.choice(self.players + ['skip'])
    
    def claimRoles(self):
        claim = Claim(self.players)
        # TODO: Random choice based on existing players
        for player in self.players:
            claim.make_claim(player, random.choice(['villager', 'werewolf', 'seer', 'witch']))
        return claim

    def lastWord(self):
        return Claim(self.players)
    