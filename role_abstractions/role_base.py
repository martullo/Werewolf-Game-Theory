from abc import ABC, abstractmethod
from typing import Union


class RoleBase(ABC):
    """
    Base class for all roles. Used to define each role's strategy.
    """
    _counter = 0

    def __init__(self, roles: dict, name: str):
        self.name = name
        self.id = RoleBase._counter
        RoleBase._counter += 1
        self.strategy = None
        self.belief_table = self.init_belief_table(roles)

    def __str__(self):
        return f"{self.name} (id {self.id})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self.id
        
    def __eq__(self, other):
        if not isinstance(other, RoleBase):
            return False
        return self.id == other.id
    
    def init_belief_table(self,roles):
        total_players = sum(roles.values())
        num_werewolf = roles['werewolf']
        num_villager = roles['villager']
        num_witch = roles['witch']
        num_seer = roles['seer']
        belief_table = dict()
        probability_ww = float(num_werewolf / total_players)
        for i in range(total_players):
            belief_table[i] = probability_ww
        return belief_table



    @abstractmethod
    def reactToDeath(self, player: int) -> None:
        """
        Abstract method to define how the role reacts to a player's death.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def claimRoles(self):
        """
        Abstract method to define how the role makes claims about all roles in
        discussion.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def reactToClaims(self, claims: dict) -> None:
        """
        Abstract method to define how the role reacts to another player's claim.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def vote(self) -> Union["RoleBase", str]:
        """
        Abstract method to define how the role votes in discussion.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def reactToVotes(self, votes: dict, votedOutPlayer: Union[int, str]) -> None:
        """
        Abstract method to define how the role reacts to another player's vote.
        """
        raise NotImplementedError("Subclasses must implement this method.")
