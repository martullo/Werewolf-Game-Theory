from role_abstractions.role_base import RoleBase

class VillagerRoleBase(RoleBase):
    def __init__(self, roles, name: str = "villager"):
        super().__init__(roles,name)