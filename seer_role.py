from role_abstractions.seer_role_base import SeerRoleBase

class SeerRole(SeerRoleBase):
    """
    Seer role implementation.
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

    def choosePlayerToCheck(self):
        pass

    def updateRoleClaimsAfterSeen(self):
        pass