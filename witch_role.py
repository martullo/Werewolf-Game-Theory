from role_abstractions.witch_role_base import WitchRoleBase

class WitchRole(WitchRoleBase):
    """
    Witch role implementation.
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

    def decideSaveOrPoison(self):
        pass