from strategy_base import Strategy
import random

class RandomStrategy(Strategy):
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self):
        super().__init__("random")

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return None  

    def claimRoles(self, id, claim, players):
        for player in players:
            if player == id:
                claim.make_claim(player,'villager')
            else:
                claim.make_claim(player, random.choice(['villager', 'werewolf', 'seer', 'witch']))
        return claim
    
    def chooseVictim(self, players):
        return random.choice(players)
