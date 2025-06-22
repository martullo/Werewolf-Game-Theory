import random
import logging
import os
import tqdm
from role_abstractions.role_base import RoleBase

from villager_role import VillagerRole
from werewolf_role import WerewolfRole
from seer_role import SeerRole
from witch_role import WitchRole

from claim import Claim as PlayerClaim

# === Setup dynamic logging ===
#just comment it in to enable logging, make sure to specify a valid path
log_index = 1
while os.path.exists(f"log{log_index}.log"):
    log_index += 1

log_filename = f"log.log"
logging.basicConfig(
    filename=log_filename,
    filemode='w',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
class Game():
    def __init__(self):
        self.players = []
        self.gameRunning = True
        self.werewolves = []
        self.winner = None

    def setup_game(self, num_villagers=7, num_werewolves=3, num_seers=1, num_witches=0):
        self.players.clear()
        roles = dict()
        roles['villager'] = num_villagers
        roles['werewolf'] = num_werewolves
        roles['seer'] = num_seers
        roles['witch'] = num_witches

        for _ in range(num_villagers):
            self.players.append(VillagerRole(roles))
        for _ in range(num_werewolves):
            self.players.append(WerewolfRole(roles))
        for _ in range(num_seers):
            self.players.append(SeerRole(roles))
        for _ in range(num_witches):
            self.players.append(WitchRole(roles))

        for player in self.players:
            player.players = list(map(lambda x: x.id, self.players))

        logging.info("=== Player Roles ===")
        for player in self.players:
            logging.info(f"{player} -> {player.name}")
        
        #werewolves setup, they keep a list of their teammates, Game keeps it too
        for player in self.players:
            if isinstance(player, WerewolfRole):
                self.werewolves.append(player)
            
        for werewolf in self.werewolves:
            werewolf.werewolves = list(map(lambda x: x.id, self.werewolves))
           
            
        

    def werewolves_choose_victim(self):
        victim = self.getPlayerById(self.werewolfVictimSyndicate())
        #print(f"-> Werewolves chose victim: {victim}")
        logging.info("=========NIGHT VICTIM=========")
        logging.info(f"Werewolves chose victim: {victim}")
        logging.info("===================")
        return victim
    def seer_checks_player(self):
        checkPlayer = None
        for player in self.players:
                if isinstance(player, SeerRole):
                    print(player.choosePlayerToCheck())
                    checkPlayer = self.getPlayerById(player.choosePlayerToCheck())
                    #print(f"-> Seer chose to check: {checkPlayer}")
                    logging.info(f"Seer {player} checked: {checkPlayer}")
                    player.updateRoleClaimsAfterSeen(checkPlayer.id, checkPlayer.name) #seer updates her claims
        return checkPlayer
    
    def witch_action(self):
        pass
        """
        poisonedPlayers = []
        for player in self.players:
            if isinstance(player, WitchRole):
                poisonedPlayers.append(getPlayerById(player.decideSaveOrPoison(victim.id)))
        """
    def discussion(self):
        claims = {}
        for player in self.players:
            claims[player.id] = player.claimRoles()
            #print(f"-> {player} claims: {claims[player.id]}")
            logging.info(f"-> {player} claims: {claims[player.id]}")
        for player in self.players:
            player.reactToClaims(claims)
    
    def voting(self):
        votes = {'skip': 0}
        for player in self.players:
            vote = player.vote()
            #print(f"-> {player} votes for: {vote}")
            if vote not in votes:
                votes[vote] = 1
            else:
                votes[vote] += 1


        for player in self.players:
            player.reactToVotes(votes, 'skip')

        voted_out_id = max(votes, key=votes.get)
        votedOutPlayer = 'skip' if voted_out_id == 'skip' else self.getPlayerById(voted_out_id)
        candidates = [player for player in self.players if votes.get(player.id, 0) == max(votes.values())]
        
        if list(votes.values()).count(max(votes.values())) > 1:
            #print(f"-> Tie between {candidates}, no player voted out.")
            logging.info(f"Votes: {votes}")
            logging.info(f"-> Tie between {candidates}") 
            logging.info("===================")
            if 'skip' in candidates:
                candidates.remove('skip')
            #for now we ignore skip, random candidate dies
            votedOutPlayer = random.choice(candidates)
            victim = votedOutPlayer  # None
            logging.info(f"-> {votedOutPlayer} voted out.")
        elif votedOutPlayer == 'skip':
            #print("-> No player voted out, skipping.")
            logging.info("No player voted out (skip).")
            logging.info("===================")
            victim = None
        else:
            #print(f"-> Player voted out during the day: {votedOutPlayer}")
            logging.info(f"Player voted out: {votedOutPlayer}")
            logging.info("===================")
            victim = votedOutPlayer

        if isinstance(votedOutPlayer, RoleBase) and votedOutPlayer != 'skip':
            votedOutPlayerClaim = votedOutPlayer.lastWord().claims
            
            logging.info(f"Last Words -> {votedOutPlayer} claims: {votedOutPlayerClaim}")
            for player in self.players:
                player.reactToDeath(votedOutPlayerClaim)

        if victim is not None:
            try:
                self.players.remove(victim)
            except ValueError:
                pass
        for player in self.players:
            player.players = list(map(lambda x: x.id, self.players))
        """
        if votedOutPlayer != 'skip':
            try:
                self.players.remove(votedOutPlayer)
            except ValueError:
                pass
        """

    
    def play_game(self):
        for player in self.players:
            player.players = list(map(lambda x: x.id, self.players))

        while self.gameRunning:
            

            #print("§ Discussion §")
            self.discussion()

            #print("§ Voting §")
            self.voting()
            self.checkGameOver()
            if not self.gameRunning:
                break
            victim = self.werewolves_choose_victim()

            #seer checks a player
            checkPlayer = self.seer_checks_player()
            
            poisonedPlayers = self.witch_action()
            
                
            #a person dies and leaves a last word and everyone updates theie claims (atm only seer influences the claims)
            dead_claims = dict()
            if victim is not None:
                if isinstance(victim, RoleBase):
                    dead_claims = victim.lastWord().claims
                    logging.info(f"-> Night victim {victim} claims: {dead_claims}")
                    self.players.remove(victim)
                    #print(f"Last Words -> {votedOutPlayer} claims: {votedOutPlayerClaim}")
            for player in self.players:
                if victim is not None:
                    if dead_claims:
                        player.reactToDeath(dead_claims) #we pass claims here, if there is a claim like 10: seer, we know seer died, we update accordingly, this simulates opening up at death and since we reveal the roles after death no additional functionality needed
                    player.players.remove(victim.id)
                """
                for poisonedPlayer in poisonedPlayers:
                    player.reactToDeath(poisonedPlayer.id)
                """
            self.checkGameOver()
            if not self.gameRunning:
                break
            


    def werewolfVictimSyndicate(self):
        potVictims = []
        for player in self.players:
            if isinstance(player, WerewolfRole):
                potVictims.append(player.chooseVictim())
        return random.choice(potVictims)

    def getPlayerById(self,playerId):
        for player in self.players:
            if player.id == playerId:
                return player

    def checkGameOver(self):
        
        numVillagers = sum(1 for player in self.players if isinstance(player, VillagerRole))
        numWerewolves = sum(1 for player in self.players if isinstance(player, WerewolfRole))
        numWitches = sum(1 for player in self.players if isinstance(player, WitchRole))
        numSeers = sum(1 for player in self.players if isinstance(player, SeerRole))

        if (numSeers + numWitches + numVillagers <= numWerewolves):
            #print("WEREWOLFS WIN!")
            logging.info("Game Over: Werewolves win")
            self.logRemainingPlayers()
            self.gameRunning = False
            self.winner = "Werewolves"
        elif numWerewolves == 0:
            #print("VILLAGERS WIN!")
            logging.info("Game Over: Villagers win")
            self.logRemainingPlayers()
            self.gameRunning = False
            self.winner = "Villagers"

    def logRemainingPlayers(self):
        #print("\n=== Game Over ===")
        #print("Remaining players:")
        for p in self.players:
            #print(f"{p} ({p.name})")
            logging.info(f"Remaining: {p} ({p.name})")
        #print("=================")

if __name__ == "__main__":
    w = 0
    v = 0
    #use tqdm to show progress bar
    #print("Starting 100,000 games...")
    gameRunning = True
    #print("Press Ctrl+C to stop the simulation at any time.")
    i = 100
    for _ in tqdm.tqdm(range(i)):
        RoleBase._counter = 0
        game = Game()
        game.setup_game(num_villagers=120,num_werewolves=5,num_seers=0)
        game.play_game()
        if game.winner == "Werewolves":
            w += 1
        elif game.winner == "Villagers":
            v += 1

    print(f"After {i} games: {w} Werewolves win, {v} Villagers win.")