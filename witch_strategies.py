from strategy_base import Strategy
class BasicStrategy(Strategy):
    

    def __init__(self):
        super().__init__("basic")

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        pass
    def decideSaveOrPoison(self, player):
        return player
    def open_up(self):
        pass

class SomeStrategy(Strategy):
    """
    Example of a more complex strategy.
    """
    
    def __init__(self):
        super().__init__("some_strategy")

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        pass
    
    def decideSaveOrPoison(self, player):
        return player
    
    def open_up(self):
        pass
