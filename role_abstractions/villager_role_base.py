from role_abstractions.role_base import RoleBase

class VillagerRoleBase(RoleBase):
    def __init__(self, name: str = "Villager"):
        super().__init__(name)