from roleBase import RoleBase

class SeerRoleBase(RoleBase):
    """
    Base class for Seer role.
    """

    def __init__(self, numPlayers: int, name: str = "Seer"):
        super().__init__(name, numPlayers)

    @abstractmethod
    def choosePlayerToCheck(self):
        """
        Abstract method to define the Seer's strategy to choose a player to check.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def updateRoleClaims(self):
        """
        Abstract method to define the Seer's strategy to update it's claims based on
        the checked player.
        """
        raise NotImplementedError("Subclasses must implement this method.")