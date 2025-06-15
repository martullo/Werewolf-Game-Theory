from role_abstractions.witch_role_base import WitchRoleBase

class WitchRole(WitchRoleBase):
    """
    Witch role implementation.
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

    def decideSaveOrPoison(self):
        pass