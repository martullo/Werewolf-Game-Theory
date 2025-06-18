from abc import ABC, abstractmethod

from role_abstractions.role_base import RoleBase

class WitchRoleBase(RoleBase):
    """
    Base class for Witch role.
    """

    def __init__(self, name: str = "Witch"):
        super().__init__(name)

    @abstractmethod
    def decideSaveOrPoison(self) -> "RoleBase":
        """
        Abstract method to define the Witch's strategy to decide to save the player
        or poison another.
        """
        raise NotImplementedError("Subclasses must implement this method.")