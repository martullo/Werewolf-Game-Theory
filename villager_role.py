import random

from role_abstractions.villager_role_base import VillagerRoleBase
import villager_strategy
from claim import Claim

class VillagerRole(VillagerRoleBase):
    """
    Random villager role implementation.
    """

    def __init__(self):
        super().__init__()
        self.players = None # This will be set by the game manager after every round
        self.strategy = villager_strategy.RandomStrategy()
    def reactToDeath(self, player):
        pass
    
    def claimRoles(self):
        claim = Claim(self.players)
        claim = self.strategy.claimRoles(self.id, claim, self.players)
        return claim

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return random.choice(self.players + ['skip'])
    
    def reactToVotes(self, votes, votedOutPlayer):
        pass
    