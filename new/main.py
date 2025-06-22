import logging
import os
import tqdm

import random

import villager_strategies
import werewolf_strategies
import seer_strategies
import witch_strategies

from claim import Claim

# === Setup dynamic logging ===
#just comment it in to enable logging, make sure to specify a valid path
log_index = 1
strategies_printed = False
while os.path.exists(f"log{log_index}.log"):
    log_index += 1
log_filename = f"logNew.log"
logging.basicConfig(
    filename=log_filename,
    filemode='w',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

class Game:
    def __init__(self):
        self.players = []
        self.gameRunning = True
        self.werewolves = []
        self.winner = None

    def setup_game(self, n_vil=7, n_wer=3, n_see=1, n_wit=1):
        global strategies_printed
        self.players.clear()
        for i in range(n_vil):
            self.players.append(villager_strategies.TrustStrategy(i))
        for i in range(n_wer):
            self.players.append(werewolf_strategies.BeastStrategy(n_vil + i))
        for i in range(n_see):
            self.players.append(seer_strategies.FirstWerewolfStrategy(n_vil + n_wer + i))
        for i in range(n_wit):
            self.players.append(witch_strategies.RandomStrategy(n_vil + n_wer + n_see + i))
        
        for player in self.players:
            player.claims = Claim(list(map(lambda x: x.id, self.players)))
        if not strategies_printed:
            strategies = set()
            for player in self.players:
                strategies.add(type(player))

            print("Game initialized with the following stratagies: ", strategies)
            logging.info(f"Game initialized with the following stratagies: , {strategies}")
            strategies_printed = True
        logging.info("=== Player Roles ===")
        for player in self.players:
            logging.info(f"{player}")

        #werewolves setup, they keep a list of their teammates, Game keeps it too
        for player in self.players:
            player.roles = {"villager": n_vil, "werewolf": n_wer, "seer": n_see, "witch": n_wit}
            if isinstance(player, werewolf_strategies.BeastStrategy):
                self.werewolves.append(player)
            
        for werewolf in self.werewolves:
            werewolf.werewolves = list(map(lambda x: x.id, self.werewolves))
            # TODO
            # for w in self.werewolves:
            #     w.belief_table[w.id] = 1.0

    def werewolves_choose_victim(self):
        potVictims = []
        for player in self.players:
            if isinstance(player, werewolf_strategies.BeastStrategy):
                potVictims.append(self.getPlayerById(player.chooseVictim()))
        victim = random.choice(potVictims)
        logging.info("=========NIGHT VICTIM=========")
        logging.info(f"Werewolves chose victim: {victim}")
        logging.info("===================")
        return victim

    def seer_checks_player(self):
        checkedPlayers = []
        for player in self.players:
            if isinstance(player, seer_strategies.FirstWerewolfStrategy):
                to_check = player.choosePlayerToCheck()
                checkedPlayers.append(to_check)
                role = self.getPlayerById(to_check).role
                logging.info(f"Seer {player} checked: {to_check} with {role}")
                player.updateRoleClaimsAfterSeen(to_check, self.getPlayerById(to_check).role) #seer updates her claims
        return checkedPlayers
    
    def witch_ability(self, victim):
        poisonedPlayers = set()
        for player in self.players:
            if isinstance(player, witch_strategies.RandomStrategy):
                poisonedP = player.decideSaveOrPoison(victim)
                poisonedPlayers.add(poisonedP)
                if poisonedP == victim:
                    logging.info(f"{player} saved: the victim {victim}")
        return poisonedPlayers
    
    def discussion_phase(self):
        claims = []
        for player in self.players:
            curr_claim = player.claimRoles()
            claims.append(curr_claim)
            logging.info(f"-> {player} claims: {curr_claim}")
        for player in self.players:
            player.reactToClaims(claims)

        # For testing of seer/witch mechanism
        # if len(self.players) == 12:
        #     testClaimWitch = Claim(self.players)
        #     testClaimWitch.make_claim(10, "witch")
        #     testClaimWitch.make_claim(1, "villager")
        #     testClaimSeer = Claim(self.players)
        #     testClaimSeer.make_claim(11, "seer")
        #     testClaimSeer.make_claim(10, "witch")
        #     for player in self.players:
        #         player.reactToClaims([Claim(self.players)])

    def voting_phase(self):
        votes = {'skip': 0}
        for player in self.players:
            vote = player.vote()
            logging.info(f"{player} votes for: {vote}")
            if vote not in votes:
                votes[vote] = 1
            else:
                votes[vote] += 1
        #votes['skip'] = 0
        voted_out_id = max(votes, key=votes.get)
        votedOutPlayer = 'skip' if voted_out_id == 'skip' else self.getPlayerById(voted_out_id)
        candidates = [player for player in self.players if votes.get(player.id, 0) == max(votes.values())]
    
        if len(candidates) > 1:
            logging.info(f"Votes: {votes}")
            logging.info(f"-> Tie between {candidates}") 
            logging.info("===================")
            if 'skip' in candidates:
                candidates.remove('skip')
            votedOutPlayer = random.choice(candidates)
            logging.info(f"-> {votedOutPlayer} voted out.")
        elif votedOutPlayer == 'skip':
            logging.info("No player voted out (skip).")
            logging.info("===================")
        else:
            logging.info(f"Player voted out: {votedOutPlayer}")
            logging.info("===================")
        
        # for player in self.players:
        #     player.reactToVotes(votes, voted_out_id)
        
        if votedOutPlayer != 'skip':
            last_words = votedOutPlayer.lastWord()
            logging.info(f"Last Words -> {votedOutPlayer} claims: {last_words}")
            for player in self.players:
                player.reactToDeath(last_words)

            self.players.remove(votedOutPlayer)
            
            
            for player in self.players:
                #player.players = list(map(lambda x: x.id, self.players))
                player.players.remove(votedOutPlayer.id)  # Remove victim from other players' views"""

    def play_game(self):
        for player in self.players:
            player.players = list(map(lambda x: x.id, self.players))

        while self.gameRunning:
            

            self.discussion_phase()

            self.voting_phase()

            self.checkGameOver()
            if not self.gameRunning:
                break
            victim = self.werewolves_choose_victim()

            checkedPlayers = self.seer_checks_player()

            poisonedPlayers = self.witch_ability(victim)

            if victim in poisonedPlayers:
                poisonedPlayers.remove(victim)
                logging.info(f"Victim {victim} was saved by one or more witches.")
            else:
                victim_last_words = victim.lastWord()
                logging.info(f"Victim's last words: {victim_last_words}")
                self.players.remove(victim)
                for player in self.players:
                    player.reactToDeath(victim_last_words)
                    player.players.remove(victim.id)  # Remove victim from other players' views
            
            # TODO: Remove poisoned players from game

            self.checkGameOver()
            if not self.gameRunning:
                break


    def checkGameOver(self):
        numVillagers = sum(1 for player in self.players if isinstance(player, villager_strategies.TrustStrategy))
        numWerewolves = sum(1 for player in self.players if isinstance(player, werewolf_strategies.BeastStrategy))
        numWitches = sum(1 for player in self.players if isinstance(player, witch_strategies.RandomStrategy))
        numSeers = sum(1 for player in self.players if isinstance(player, seer_strategies.FirstWerewolfStrategy))

        if (numSeers + numWitches + numVillagers <= numWerewolves):
            logging.info("Game Over: Werewolves win")
            self.logRemainingPlayers()
            self.gameRunning = False
            self.winner = "Werewolves"
        elif numWerewolves == 0:
            logging.info("Game Over: Villagers win")
            self.logRemainingPlayers()
            self.gameRunning = False
            self.winner = "Villagers"
        
    def logRemainingPlayers(self):
        for p in self.players:
            logging.info(f"Remaining: {p}")
    
    def getPlayerById(self, player_id):
        for player in self.players:
            if player.id == player_id:
                return player
        return None


if __name__ == "__main__":
    w = 0
    v = 0
    gameRunning = True
    i = 1000
    for _ in tqdm.tqdm(range(i)):
        game = Game()
        game.setup_game(n_vil=13, n_wer=2, n_see=1, n_wit=0)
        game.play_game()
        if game.winner == "Werewolves":
            w += 1
        elif game.winner == "Villagers":
            v += 1

    print(f"After {i} games: {w} Werewolves win, {v} Villagers win.")