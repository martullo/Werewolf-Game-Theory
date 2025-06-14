from roleBase import RoleBase

class werewolfRoleBase(RoleBase):
    """
    Base class for werewolf role.
    """

    def __init__(self, numPlayers: int, name: str = "Werewolf"):
        super().__init__(name, numPlayers)

    @abstractmethod
    def chooseVictim(self):
        """
        Abstract method to define the Werewolf's strategy to choose a victim.
        """
        raise NotImplementedError("Subclasses must implement this method.")