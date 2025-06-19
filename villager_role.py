import random

from role_abstractions.villager_role_base import VillagerRoleBase

from claim import Claim

class VillagerRole(VillagerRoleBase):
    """
    Random villager role implementation.
    """

    def __init__(self):
        super().__init__()
        self.players = None # This will be set by the game manager after every round

    def reactToDeath(self, player):
        pass
    
    def claimRoles(self):
        claim = Claim(self.players)
        for player in self.players:
            claim.make_claim(player, random.choice(['villager', 'werewolf', 'seer', 'witch']))
        return claim
    
    def reactToClaims(self, claims):
        pass

    def vote(self):
        return random.choice(self.players + ['skip'])
    
    def reactToVotes(self, votes, votedOutPlayer):
        pass
    