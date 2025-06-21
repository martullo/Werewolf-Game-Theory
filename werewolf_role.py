import random

from role_abstractions.werewolf_role_base import WerewolfRoleBase

from claim import Claim
import werewolf_strategy

class WerewolfRole(WerewolfRoleBase):
    """
    Random werewolf role implementation.
    """

    def __init__(self,roles):
        super().__init__(roles)
        self.players = None # This will be set by the game manager after every round
        self.strategy = werewolf_strategy.RandomStrategyNoFriendlyFire() 
        self.is_revealed = False
        self.werewolves = []

    def reactToDeath(self, player):
        pass
    
    def claimRoles(self):
        claim = Claim(self.players)
        claim = self.strategy.claimRoles(self.id, claim, self.players, self.is_revealed)
        return claim
    
    def reactToClaims(self, claims):
        pass

    def vote(self):
        return random.choice(self.players + ['skip'])
    
    def reactToVotes(self, votes, votedOutPlayer):
        pass

    def chooseVictim(self) -> int:
        return self.strategy.chooseVictim(self.werewolves, self.players)
    def lastWord(self):
        self.is_revealed = True
        return self.claimRoles()