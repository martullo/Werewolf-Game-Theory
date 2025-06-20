import random

from role_abstractions.seer_role_base import SeerRoleBase

from claim import Claim

class SeerRole(SeerRoleBase):
    """
    Random seer role implementation.
    """

    def __init__(self, strategy):
        super().__init__()
        self.players = None # This will be set by the game manager after every round
        self.strategy = self.getStrategyByName(strategy)
        self.strategies = {}
    def reactToDeath(self, player: int):
        pass

    def getStrategyByName(self,strategy):
        match strategy:
            case "basic":
                return self.strategies.get("basic",None)
            case _:
                return self.strategies.get("basic",None)
            
            
    def claimRoles(self):
        claim = Claim(self.players)
        for player in self.players:
            claim.make_claim(player, random.choice(['villager', 'werewolf', 'seer', 'witch']))
        return claim
    
    def reactToClaims(self, claims):
        pass

    def vote(self):
        return random.choice(self.players + ['skip'])
    
    def reactToVotes(self, votes, votedOutPlayer: int):
        pass

    def choosePlayerToCheck(self):
        return random.choice(self.players)

    def updateRoleClaimsAfterSeen(self, player: int, role: str):
        pass