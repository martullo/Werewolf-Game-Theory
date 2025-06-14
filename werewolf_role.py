from role_abstractions.werewolf_role_base import WerewolfRoleBase

class WerewolfRole(WerewolfRoleBase):
    """
    Werewolf role implementation.
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

    def chooseVictim(self):
        pass