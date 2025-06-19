import random

from role_abstractions.role_base import RoleBase

from villager_role import VillagerRole
from werewolf_role import WerewolfRole
from seer_role import SeerRole
from witch_role import WitchRole

from claim import Claim as PlayerClaim

gameRunning = True
players = []

# Notes:
# - We decided on an initial day phase. What exactly does it entail? Just a
#   discussion but no voting?
def game():
    global gameRunning
    players.clear()
    players.extend([
        # 6 Villagers
        VillagerRole(),
        VillagerRole(),
        VillagerRole(),
        VillagerRole(),
        VillagerRole(),
        VillagerRole(),
        # 3 Werewolves
        WerewolfRole(),
        WerewolfRole(),
        WerewolfRole(),
        # 1 Seer
        SeerRole(),
        # 1 Witch
        WitchRole()
    ])

    for player in players:
        player.players = list(map(lambda x : x.id, players))

    while gameRunning:

        for player in players:
            player.players = list(map(lambda x : x.id, players))

        input("Press Enter to start the next round...")
        # --- Night Phase
        print("NIGHT PHASE")

        # Werewolfs choose victim
        victim = getPlayerById(werewolfVictimSyndicate())

        print(f"-> Werewolves chose victim: {victim}")

        # Seer(s) check a player
        for player in players:
            if isinstance(player, SeerRole):
                checkPlayer = getPlayerById(player.choosePlayerToCheck())
                print(f"-> Seer chose to check: {checkPlayer}")
                player.updateRoleClaimsAfterSeen(checkPlayer.id, checkPlayer.name)

        # Witch(es) sees killed player and chooses to save them or poison another player
        poisonedPlayers = []
        for player in players:
            if isinstance(player, WitchRole):
                poisonedPlayers.append(getPlayerById(player.decideSaveOrPoison(victim.id)))
        for player in poisonedPlayers:
            if player is victim:
                print(f"-> {player} was saved by Witch!")
                victim = None
                poisonedPlayers.remove(player)
            else:
                print(f"-> {player} was poisoned by Witch!")


        # --- Day Phase
        print("DAY PHASE")

        # Game reveals who died during the night
        for player in players:
            if victim is not None:
                player.reactToDeath(victim.id)
            for poisonedPlayer in poisonedPlayers:
                player.reactToDeath(poisonedPlayer.id)

        # --- --- Discussion Phase
        print("§ Discussion §")

        # Players (including killed) make claims about all roles
        claims = {}
        for player in players:
            claims[player.id] = player.claimRoles()  # Each player claims roles
            print(f"-> {player} claims: {claims[player.id]}")
        
        for player in players:
            player.reactToClaims(claims)  # Each player reacts to claims

        # --- --- Voting Phase
        print("§ Voting §")
        # Alive players vote to kill player or skip (tie is skip)
        votes = {'skip': 0}
        for player in players:
            vote = player.vote()  # Each player votes
            print(f"-> {player} votes for: {vote}")
            if vote not in votes:
                votes[vote] = 1
            votes[vote] += 1

        for player in players:
            player.reactToVotes(votes, 'skip')

        # Voted out player is announced
        votedOutPlayer = getPlayerById(max(votes, key=votes.get))  # Player with most votes
        if list(votes.values()).count(max(votes.values())) > 1 or votedOutPlayer == 'skip':
            print("-> Tie or skip, no player voted out.")
            votedOutPlayer = 'skip'
        else:
            print(f"-> Voted out player: {votedOutPlayer}")

        # Voted out player gets to claim all players role
        if isinstance(votedOutPlayer, RoleBase) and not votedOutPlayer == 'skip':
            votedOutPlayerClaim = {
                votedOutPlayer: votedOutPlayer.claimRoles()
            }
            print(f"-> {votedOutPlayer} claims: {votedOutPlayerClaim}")
            for player in players:
                player.reactToClaims(votedOutPlayerClaim)

        # Remove killed, poisoned, and voted out players from the game
        for player in poisonedPlayers:
            if player is not victim:
                players.remove(player)  # Remove poisoned player from the game
            else:
                victim = None
        if victim is not None:
            players.remove(victim)  # Remove victim from the game
        if votedOutPlayer != 'skip':
            try:
                players.remove(votedOutPlayer)  # Remove voted out player from the game
            except ValueError:
                pass

        # Check if the game is over
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
    numVillagers = sum(1 for player in players if isinstance(player, VillagerRole))
    numWerewolves = sum(1 for player in players if isinstance(player, WerewolfRole))
    numWitches = sum(1 for player in players if isinstance(player, WitchRole))
    numSeers = sum(1 for player in players if isinstance(player, SeerRole))

    if (numSeers + numWitches + numVillagers <= numWerewolves):
        print("WEREWOLFS WIN!")
        gameRunning = False
    elif numWerewolves == 0:
        print("VILLAGERS WIN!")
        gameRunning = False

if __name__ == "__main__":
    game()
