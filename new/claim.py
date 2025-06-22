

class Claim():
    def __init__(self, players: list[int]):
        self.players = players
        self.claims = dict()
        self.size = 0

    def __str__(self):
        return f"{self.claims}"
    
    def __repr__(self):
        return self.__str__()

    def make_claim(self, player: int, claimed_role: str):
        """
        Player makes a claim about their role.
        :param player: The player the claim is on.
        :param claimed_role: The role claimed on the player.
        """
        if player in self.players:
            self.claims[player] = claimed_role
        else:
            raise ValueError(f"{player} is not a valid player in this game.")
        self.size = len(self.claims.keys())
    
    def get_claim(self, player: int) -> str:
        """
        Get the claim made on a player.
        :param player: The player on which the claim is made.
        :return: The claimed role of the player as a string.
        """
        if player in self.players:
            return self.claims.get(player, None)
        else:
            raise ValueError(f"{player} is not a valid player in this game.")
        
    def get_size(self):
        return self.size