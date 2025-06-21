import random

from role_abstractions.seer_role_base import SeerRoleBase
import seer_strategy
from claim import Claim

class SeerRole(SeerRoleBase):
    """
    Random seer role implementation.
    """

    def __init__(self,roles):

        super().__init__(roles)
        self.players = None # This will be set by the game manager after every round
        self.strategies = {}
        self.is_revealed = False
        self.checked_players = dict()
        self.strategy = seer_strategy.RandomStrategyAdvanced()
    def reactToDeath(self, player: int):
        pass

    def lastWord(self):
        self.is_revealed = True
        
        return self.claimRoles()
            


        
    def claimRoles(self):
        
        claim = Claim(self.players)
        claim = self.strategy.claimRoles(self.id, claim, self.players, self.checked_players, self.is_revealed)
        return claim
    
    def reactToClaims(self, claims):
        pass

    def vote(self):
        return random.choice(self.players + ['skip'])
    
    def reactToVotes(self, votes, votedOutPlayer: int):
        pass

    def choosePlayerToCheck(self):
        return self.strategy.choosePlayerToCheck(self.players,self.checked_players,self.id)

    def updateRoleClaimsAfterSeen(self, player: int, role: str):
        self.checked_players[player] = role


    
       