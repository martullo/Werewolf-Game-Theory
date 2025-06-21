import random

from role_abstractions.villager_role_base import VillagerRoleBase
import villager_strategy
from claim import Claim

class VillagerRole(VillagerRoleBase):
    """
    Random villager role implementation.
    """

    def __init__(self,roles):
        super().__init__(roles)
        self.players = None # This will be set by the game manager after every round
        self.strategy = villager_strategy.RandomStrategy()
        self.is_revealed = False

    def reactToDeath(self, claim:dict):
        #we assume rwe trust the seer no matter what strategy, can be moved to strategy though; but atm part of "base strategy"
        if 'seer' in claim.values(): #need to implement that seer only claims the roles about 100% checked players
            print("seer died")
            for k in claim.keys():
                if claim[k] == 'werewolf':
                    self.belief_table[k] = 1.0 #probability of being werewolf for that player is 1.0
    
    def claimRoles(self):
        claim = Claim(self.players)
        claim = self.strategy.claimRoles(self.id, claim, self.players, self.belief_table,self.is_revealed)
        return claim

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return random.choice(self.players + ['skip'])
    
    def reactToVotes(self, votes, votedOutPlayer):
        pass
    def lastWord(self):
        self.is_revealed = True
        return self.claimRoles()