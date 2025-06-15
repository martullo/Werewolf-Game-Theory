from role_abstractions.villager_role_base import VillagerRoleBase

class VillagerRole(VillagerRoleBase):
    """
    Villager role implementation.
    """

    def __init__(self):
        super().__init__()

    def reactToDeath(self, player):
        pass
    
    def claimRoles(self):
        pass
    
    def reactToClaims(self, claims):
        pass

    def vote(self):
        pass
    
    def reactToVotes(self, votes, votedOutPlayer):
        pass
    