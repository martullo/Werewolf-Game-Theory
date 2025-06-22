from claim import Claim
import random
import logging
import copy
class SilentStrategy:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self, id):
        self.role:str = 'seer'
        self.players:list[int] = None  # This will be set by the game manager after every round
        self.id:int = id  # Player ID, to be set by the game manager
        self.claims:Claim = None
        self.is_revealed:bool = False
        self.checked_players: dict[int,str] = dict()

    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)

    def vote(self):
        return None  

    def claimRoles(self):
        claim = Claim(self.players)
        # for player in self.players:
        #     if player == self.id:
        #         claim.make_claim(player, 'seer')
        #     else:
        #         claim.make_claim(player, random.choice(['villager', 'werewolf', 'witch']))
        if self.is_revealed:
            alive_player_ids = self.players
            claim.make_claim(self.id, 'seer')  # Claiming self as seer
            for player, role in self.checked_players.items():
                if player in alive_player_ids:
                    claim.make_claim(player,role)
        return claim
        # return Claim(self.players)


    def reveal(self):
        logging.info("SEER REVELED HERSELF")
        self.is_revealed = True

    def choosePlayerToCheck(self):
        return random.choice(self.players)

    def updateRoleClaimsAfterSeen(self, player: int, role: str):
        self.checked_players[player] = role
    
    def lastWord(self):
        self.reveal()
        claim = self.claimRoles()
        
        return [claim]



class SilentStrategyAdvanced:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self, id):
        self.role:str = 'seer'
        self.players:list[int] = None  # This will be set by the game manager after every round
        self.id:int = id  # Player ID, to be set by the game manager
        self.claims:Claim = None
        self.is_revealed:bool = False
        self.checked_players: dict[int,str] = dict()

    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)

    def vote(self):
        return None  

    def claimRoles(self):
        claim = Claim(self.players)
        # for player in self.players:
        #     if player == self.id:
        #         claim.make_claim(player, 'seer')
        #     else:
        #         claim.make_claim(player, random.choice(['villager', 'werewolf', 'witch']))
        if self.is_revealed:
            alive_player_ids = self.players
            claim.make_claim(self.id, 'seer')  # Claiming self as seer
            for player, role in self.checked_players.items():
                if player in alive_player_ids:
                    claim.make_claim(player,role)
        return claim
        # return Claim(self.players)


    def reveal(self):
        logging.info("SEER REVELED HERSELF")
        self.is_revealed = True

    def choosePlayerToCheck(self):
        to_check = copy.deepcopy(self.players)
        to_check.remove(self.id)
        for p in self.checked_players.keys():
            if p in to_check:
                to_check.remove(p) #no double checking
        if len(to_check)==0:
            return random.choice(self.players) #if we checked everyone, we don't care anymore
        return random.choice(to_check)

    def updateRoleClaimsAfterSeen(self, player: int, role: str):
        self.checked_players[player] = role
    
    def lastWord(self):
        self.reveal()
        claim = self.claimRoles()
        
        return [claim]




class RandomStrategy:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self, id):
        self.role:str = 'seer'
        self.players:list[int] = None  # This will be set by the game manager after every round
        self.id:int = id  # Player ID, to be set by the game manager
        self.claims:Claim = None
        self.is_revealed:bool = False
        self.checked_players: dict[int,str] = dict()

    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)

    def vote(self):
        return None  

    def claimRoles(self):
        claim = Claim(self.players)

        random_reveal = random.random()
        if random_reveal >= 0.5:
            self.reveal()
        # for player in self.players:
        #     if player == self.id:
        #         claim.make_claim(player, 'seer')
        #     else:
        #         claim.make_claim(player, random.choice(['villager', 'werewolf', 'witch']))
        if self.is_revealed:
            alive_player_ids = self.players
            claim.make_claim(self.id, 'seer')  # Claiming self as seer
            for player, role in self.checked_players.items():
                if player in alive_player_ids:
                    claim.make_claim(player,role)
        return claim
        # return Claim(self.players)


    def reveal(self):
        logging.info("SEER REVELED HERSELF")
        self.is_revealed = True

    def choosePlayerToCheck(self):
        return random.choice(self.players)

    def updateRoleClaimsAfterSeen(self, player: int, role: str):
        self.checked_players[player] = role
    
    def lastWord(self):
        self.reveal()
        claim = self.claimRoles()
        
        return [claim]
    

class FirstWerewolfStrategy:
    """
    Random strategy implementation.
    This strategy randomly chooses actions without any specific logic.
    """

    def __init__(self, id):
        self.role:str = 'seer'
        self.players:list[int] = None  # This will be set by the game manager after every round
        self.id:int = id  # Player ID, to be set by the game manager
        self.claims:Claim = None
        self.is_revealed:bool = False
        self.checked_players: dict[int,str] = dict()

    def __str__(self):
        return f"{self.role} (id {self.id})"
    
    def __repr__(self):
        return self.__str__()

    def reactToDeath(self, player):
        pass

    def reactToClaims(self, claims):
        for claim in claims:
            plainClaim = claim.claims
            if 'witch' in plainClaim.values():
                for (player, role) in plainClaim.items():
                    if role is not None:
                        self.claims.make_claim(player, role)

    def vote(self):
        return None  

    def claimRoles(self):
        claim = Claim(self.players)

        
    
        if self.is_revealed:
            alive_player_ids = self.players
            claim.make_claim(self.id, 'seer')  # Claiming self as seer
            for player, role in self.checked_players.items():
                if player in alive_player_ids:
                    claim.make_claim(player,role)
        return claim


    def reveal(self):
        logging.info("SEER REVELED HERSELF")
        self.is_revealed = True

    def choosePlayerToCheck(self):
        return random.choice(self.players)

    def updateRoleClaimsAfterSeen(self, player: int, role: str):
        self.checked_players[player] = role
        if role == 'werewolf':
            self.reveal()
    
    def lastWord(self):
        self.reveal()
        claim = self.claimRoles()
        
        return [claim]