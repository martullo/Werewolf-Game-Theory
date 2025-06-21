from strategy_base import Strategy
import random

import copy


class RandomStrategy(Strategy):
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self):
        super().__init__("open_at_death")
        self.role = 'seer'

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return None  
    
    

    def claimRoles(self, id, claim, players, checked_players, is_revealed=False):
        for player in players:
            if player == id:
                if is_revealed:
                    claim.make_claim(player,self.role)
                else:
                    claim.make_claim(player, 'villager')
            elif player in checked_players.keys():
                claim.make_claim(player, checked_players.get(player, None))
            else:
                claim.make_claim(player, random.choice(['villager']))
            
        return claim

    def reveal(self):
        return True
    def choosePlayerToCheck(self,players,checked_players,id):
        random.choice(players)



class RandomStrategyAdvanced(Strategy):
    """
    Random strategy implementation.
    Seer doesn't check herself, doesn't check same player more then once
    """

    def __init__(self):
        super().__init__("open_at_death")
        self.role = 'seer'

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        return None  
    
    

    def claimRoles(self, id, claim, players, checked_players, is_revealed=False):
        for player in players:
            if player == id:
                if is_revealed:
                    claim.make_claim(player,self.role)
                else:
                    claim.make_claim(player, 'villager')
            elif player in checked_players.keys():
                claim.make_claim(player, checked_players.get(player, None))
            else:
                claim.make_claim(player, random.choice(['villager']))
            
        return claim

    def reveal(self):
        return True
    def choosePlayerToCheck(self,players,checked_players,id):
        to_check = copy.deepcopy(players)
        to_check.remove(id)
        for p in checked_players.keys():
            if p in to_check:
                to_check.remove(p) #no double checking
        return random.choice(to_check)

