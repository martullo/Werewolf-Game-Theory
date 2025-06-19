import random

from role_abstractions.witch_role_base import WitchRoleBase

from claim import Claim

class WitchRole(WitchRoleBase):
    """
    Random witch role implementation.
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

    def decideSaveOrPoison(self, player):
        return random.choice([player] + [random.choice(self.players)])