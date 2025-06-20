from abc import ABC, abstractmethod

from role_abstractions.role_base import RoleBase

class WerewolfRoleBase(RoleBase):
    """
    Base class for werewolf role.
    """

    def __init__(self, roles: dict, name: str = "werewolf"):
        super().__init__(roles,name)

    @abstractmethod
    def chooseVictim(self):
        """
        Abstract method to define the Werewolf's strategy to choose a victim.
        """
        raise NotImplementedError("Subclasses must implement this method.")