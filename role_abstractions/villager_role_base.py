from roleBase import RoleBase

class VillagerRoleBase(RoleBase):
    def __init__(self, numPlayers: int, name: str = "Villager"):
        super().__init__(name, numPlayers)