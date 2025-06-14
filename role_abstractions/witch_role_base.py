from roleBase import RoleBase

class WitchRoleBase(RoleBase):
    """
    Base class for Witch role.
    """

    def __init__(self, numPlayers: int, name: str = "Witch"):
        super().__init__(name, numPlayers)

    @abstractmethod
    def decideSaveOrPoison(self):
        """
        Abstract method to define the Witch's strategy to decide to save the player
        or poison another.
        """
        raise NotImplementedError("Subclasses must implement this method.")