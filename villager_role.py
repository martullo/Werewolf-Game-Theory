from role_abstractions.villager_role_base import VillagerRoleBase

class VillagerRole(VillagerRoleBase):
    """
    Villager role implementation.
    """

    def __init__(self, numPlayers: int):
        super().__init__(numPlayers=numPlayers)

    def reactToDeath(self):
        pass

    def claimRolesOnKilled(self):
        pass
    
    def claimRoles(self):
        pass
    
    def vote(self):
        pass
    
    def claimRolesOnVotedOut(self):
        pass
    