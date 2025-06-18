from role_abstractions.seer_role_base import SeerRoleBase

class SeerRole(SeerRoleBase):
    """
    Seer role implementation.
    """

    def __init__(self):
        super().__init__()

    def reactToDeath(self, player: int):
        pass
    
    def claimRoles(self):
        pass
    
    def reactToClaims(self, claims):
        pass

    def vote(self):
        pass
    
    def reactToVotes(self, votes, votedOutPlayer: int):
        pass

    def choosePlayerToCheck(self):
        return 1

    def updateRoleClaimsAfterSeen(self, player: int, role: str):
        pass