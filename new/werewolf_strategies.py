from claim import Claim
import random


class RandomStrategy:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """
    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()
    
    def __init__(self, id):
        self.role = 'werewolf'
        self.players = None  # This will be set by the game manager after every round
        self.id = id  # Player ID, to be set by the game manager
        self.werewolves = []  # List of werewolf teammates, to be set by the game manager
        self.belief_table = None  # Belief table, to be set by the game manager
        self.roles = None  # Roles of players, to be set by the game manager

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        pass

    def vote(self):
        players = [p for p in self.players if p not in self.werewolves]
        return random.choice(self.players + ['skip'])

    # def claimRoles(self, id, claim, players, is_revealed=False):
    #     for player in players:

    #         if player == id:
    #             if is_revealed:
    #                 claim.make_claim(player,self.role)
    #             else:
    #                 claim.make_claim(player,'villager')
    #         else:
    #             claim.make_claim(player, random.choice(['villager']))
    #     return claim
    
    def claimRoles(self):
        claim = Claim(self.players)
        # TODO: Random choice based on existing players
        for player in self.players:
            existing_roles = [role for role in ['villager', 'werewolf', 'seer', 'witch'] if self.roles[role] > 0]
            claim.make_claim(player, random.choice(existing_roles))
        return claim
    
    def chooseVictim(self):
        players = [p for p in self.players if p not in self.werewolves]
        return random.choice(players)
    
    def lastWord(self):
        return self.claimRoles()
