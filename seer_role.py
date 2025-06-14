from role_abstractions.seer_role_base import SeerRoleBase

class SeerRole(SeerRoleBase):
    """
    Seer role implementation.
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

    def choosePlayerToCheck(self):
        pass

    def updateRoleClaims(self):
        pass