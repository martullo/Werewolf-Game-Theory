from abc import ABC, abstractmethod

from role_abstractions.role_base import RoleBase

class SeerRoleBase(RoleBase):
    """
    Base class for Seer role.
    """

    def __init__(self, roles: dict,name: str = "seer"):
        super().__init__(roles,name)
       

    @abstractmethod
    def choosePlayerToCheck(self) -> "RoleBase":
        """
        Abstract method to define the Seer's strategy to choose a player to check.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def updateRoleClaimsAfterSeen(self):
        """
        Abstract method to define the Seer's strategy to update it's claims based on
        the checked player.
        """
        raise NotImplementedError("Subclasses must implement this method.")