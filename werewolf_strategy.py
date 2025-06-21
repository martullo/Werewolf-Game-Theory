from strategy_base import Strategy
import random

class RandomStrategy(Strategy):
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self):
        super().__init__("random")
        self.role = 'werewolf'

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return None  

    def claimRoles(self, id, claim, players,is_revealed=False):
        for player in players:
            if player == id:
                if is_revealed:
                    claim.make_claim(player,self.role)
                else:
                    claim.make_claim(player,'villager')
            else:
                claim.make_claim(player, random.choice(['villager']))
        return claim

    def chooseVictim(self, werewolves, players):

        return random.choice(players)

class RandomStrategyNoFriendlyFire(Strategy):
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self):
        super().__init__("random")
        self.role = 'werewolf'

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return None  

    def claimRoles(self, id, claim, players, is_revealed=False):
        for player in players:

            if player == id:
                if is_revealed:
                    claim.make_claim(player,self.role)
                else:
                    claim.make_claim(player,'villager')
            else:
                claim.make_claim(player, random.choice(['villager']))
        return claim
    
    def chooseVictim(self, werewolves, players):
        if werewolves:
            players = [p for p in players if p not in werewolves]
        return random.choice(players)