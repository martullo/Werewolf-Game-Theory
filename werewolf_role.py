from role_abstractions.werewolf_role_base import WerewolfRoleBase

class WerewolfRole(WerewolfRoleBase):
    """
    Werewolf role implementation.
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

    def chooseVictim(self):
        pass