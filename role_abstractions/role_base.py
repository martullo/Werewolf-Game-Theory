


class RoleBase:
    """
    Base class for all roles. Used to define each role's strategy.
    """

    def __init__(self, name: str, numPlayers: int = 1):
        self.name = name
        self.numPlayers = numPlayers
    
    def __str__(self):
        return f"{self.name} with {self.numPlayers} players"

    def __repr__(self):
        return f"BaseRole(name={self.name}, numPlayers={self.numPlayers})"

    @abstractmethod
    def reactToDeath(self):
        """
        Abstract method to define how the role reacts to a player's death.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def claimRolesOnKilled(self):
        """
        Abstract method to define how the role makes claims about all roles when
        it's killed.
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
    def vote(self):
        """
        Abstract method to define how the role votes in discussion.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def claimRolesOnVotedOut(self):
        """
        Abstract method to define how the role makes claims about roles when it's
        voted out.
        """
        raise NotImplementedError("Subclasses must implement this method.")
