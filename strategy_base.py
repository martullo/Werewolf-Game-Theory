from abc import ABC, abstractmethod
class Strategy:
    """
    Base class for all strategies. Used to define each strategy's behavior.
    """
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Strategy: {self.name}"
    
    @abstractmethod
    def reactToDeath(self, player):
        pass
    @abstractmethod
    def reactToClaims(self, claims):
        raise NotImplementedError("Subclasses must implement this method.")
    @abstractmethod
    def vote(self):
        raise NotImplementedError("Subclasses must implement this method.")
