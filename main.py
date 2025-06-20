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
""" just comment it in to enable logging, make sure to specify a valid path
log_index = 1
while os.path.exists(f"log{log_index}.log"):
    log_index += 1

log_filename = f"log{log_index}.log"
logging.basicConfig(
    filename=log_filename,
    filemode='w',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
"""
#print(f"Logging to file: {log_filename}")
gameRunning = True
players = []

def game():
    global gameRunning
    players.clear()
    num_villagers = 144
    num_werewolves = 6
    num_seers = 0
    num_witches = 0

    for _ in range(num_villagers):
        players.append(VillagerRole())
    for _ in range(num_werewolves):
        players.append(WerewolfRole())
    for _ in range(num_seers):
        players.append(SeerRole("basic"))
    for _ in range(num_witches):
        players.append(WitchRole())

    for player in players:
        player.players = list(map(lambda x: x.id, players))

    logging.info("=== Player Roles ===")
    for player in players:
        #print(f"{player} -> {player.name}")
        logging.info(f"{player} -> {player.name}")
    werewolves = []
    for player in players:
        if isinstance(player, WerewolfRole):
            werewolves.append(player)
    for werewolf in werewolves:
        werewolf.werewolves = list(map(lambda x: x.id, werewolves))
    while gameRunning:
        #print(players)
        for player in players:
            player.players = list(map(lambda x: x.id, players))

        #input("Press Enter to start the next round...")

        # --- Night Phase ---
        #print("NIGHT PHASE")
        victim = getPlayerById(werewolfVictimSyndicate())
        #print(f"-> Werewolves chose victim: {victim}")
        logging.info("=========NIGHT VICTIM=========")
        logging.info(f"Werewolves chose victim: {victim}")
        logging.info("===================")

        for player in players:
            if isinstance(player, SeerRole):
                checkPlayer = getPlayerById(player.choosePlayerToCheck())
                #print(f"-> Seer chose to check: {checkPlayer}")
                logging.info(f"Seer checked: {checkPlayer}")
                player.updateRoleClaimsAfterSeen(checkPlayer.id, checkPlayer.name)

        poisonedPlayers = []
        for player in players:
            if isinstance(player, WitchRole):
                poisonedPlayers.append(getPlayerById(player.decideSaveOrPoison(victim.id)))

      
        

        # --- Day Phase ---
        #print("DAY PHASE")

        if victim is not None:
            players.remove(victim)
        for player in players:
            if victim is not None:
                player.reactToDeath(victim.id)
                player.players.remove(victim.id)
            for poisonedPlayer in poisonedPlayers:
                player.reactToDeath(poisonedPlayer.id)

        checkGameOver()
        if not gameRunning:
            break

        #print("§ Discussion §")
        claims = {}
        for player in players:
            claims[player.id] = player.claimRoles()
            #print(f"-> {player} claims: {claims[player.id]}")
        for player in players:
            player.reactToClaims(claims)

        #print("§ Voting §")
        votes = {'skip': 0}
        for player in players:
            vote = player.vote()
            #print(f"-> {player} votes for: {vote}")
            if vote not in votes:
                votes[vote] = 1
            else:
                votes[vote] += 1


        for player in players:
            player.reactToVotes(votes, 'skip')

        voted_out_id = max(votes, key=votes.get)
        votedOutPlayer = 'skip' if voted_out_id == 'skip' else getPlayerById(voted_out_id)
        candidates = [player for player in players if votes.get(player.id, 0) == max(votes.values())]
        
        if list(votes.values()).count(max(votes.values())) > 1:
            #print(f"-> Tie between {candidates}, no player voted out.")
            logging.info(f"Votes: {votes}")
            logging.info(f"-> Tie between {candidates}, no player voted out.")
            logging.info("===================")
            if 'skip' in candidates:
                candidates.remove('skip')
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
            votedOutPlayerClaim = {
                votedOutPlayer: votedOutPlayer.claimRoles()
            }
            #print(f"Last Words -> {votedOutPlayer} claims: {votedOutPlayerClaim}")
            for player in players:
                player.reactToClaims(votedOutPlayerClaim)

        if victim is not None:
            try:
                players.remove(victim)
            except ValueError:
                pass

        if votedOutPlayer != 'skip':
            try:
                players.remove(votedOutPlayer)
            except ValueError:
                pass

        checkGameOver()

def werewolfVictimSyndicate():
    potVictims = []
    for player in players:
        if isinstance(player, WerewolfRole):
            potVictims.append(player.chooseVictim())
    return random.choice(potVictims)

def getPlayerById(playerId):
    for player in players:
        if player.id == playerId:
            return player

def checkGameOver():
    global gameRunning
    global winner
    numVillagers = sum(1 for player in players if isinstance(player, VillagerRole))
    numWerewolves = sum(1 for player in players if isinstance(player, WerewolfRole))
    numWitches = sum(1 for player in players if isinstance(player, WitchRole))
    numSeers = sum(1 for player in players if isinstance(player, SeerRole))

    if (numSeers + numWitches + numVillagers <= numWerewolves):
        #print("WEREWOLFS WIN!")
        logging.info("Game Over: Werewolves win")
        logRemainingPlayers()
        gameRunning = False
        winner = "Werewolves"
    elif numWerewolves == 0:
        #print("VILLAGERS WIN!")
        logging.info("Game Over: Villagers win")
        logRemainingPlayers()
        gameRunning = False
        winner = "Villagers"

def logRemainingPlayers():
    #print("\n=== Game Over ===")
    #print("Remaining players:")
    for p in players:
        #print(f"{p} ({p.name})")
        logging.info(f"Remaining: {p} ({p.name})")
    #print("=================")

if __name__ == "__main__":
    w = 0
    v = 0
    #use tqdm to show progress bar
    #print("Starting 100,000 games...")
    winner = None   
    gameRunning = True
    #print("Press Ctrl+C to stop the simulation at any time.")
    i = 100
    for _ in tqdm.tqdm(range(i)):
        game()
        if winner == "Werewolves":
            w += 1
        elif winner == "Villagers":
            v += 1
        winner = None
        gameRunning = True

    print(f"After {i} games: {w} Werewolves win, {v} Villagers win.")