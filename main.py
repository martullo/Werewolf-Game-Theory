import random

from role_abstractions.role_base import RoleBase

from villager_role import VillagerRole
from werewolf_role import WerewolfRole
from seer_role import SeerRole
from witch_role import WitchRole

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

    while gameRunning:
        # --- Night Phase
        print("Night Phase")

        # Werewolfs choose victim
        victim = werewolfVictimSyndicate()
        print(f"Werewolves chose victim: {victim}")

        # Seer(s) choose player to check
        # Seer(s) update claims

        # Witch sees killed player and chooses to save them or poison another player

        # --- Day Phase
        print("Day Phase")

        # Game reveals who died during the night
        for player in players:
            player.reactToDeath(victim)

        # --- --- Discussion Phase
        print("§ Discussion §")

        # Players (including killed) make claims about all roles
        claims = {}
        for player in players:
            claims[player] = player.claimRoles()  # Each player claims roles
            print(f"{player} claims: {claims[player]}")
        
        for player in players:
            player.reactToClaims(claims)  # Each player reacts to claims

        # --- --- Voting Phase
        print("§ Voting §")
        # Alive players vote to kill player or skip (tie is skip)
        votes = {'skip': 0}
        for player in players:
            vote = player.vote()  # Each player votes
            print(f"{player} votes for: {vote}")
            if vote not in votes:
                votes[vote] = 0
            votes[vote] += 1

        for player in players:
            player.reactToVotes(votes, 'skip')

        # Voted out player is announced
        votedOutPlayer = max(votes, key=votes.get)  # Player with most votes
        if list(votes.values()).count(max(votes.values())) > 1 or votedOutPlayer == 'skip':
            print("Tie or skip, no player voted out.")
        else:
            print(f"Voted out player: {votedOutPlayer}")


        # Voted out player gets to claim all players role
        if not isinstance(votedOutPlayer, RoleBase) and not votedOutPlayer is None:
            votedOutPlayerClaim = {
                votedOutPlayer: votedOutPlayer.claimRoles()
            }
            print(f"{votedOutPlayer} claims: {votedOutPlayerClaim}")
            for player in players:
                player.reactToClaim(votedOutPlayer, votedOutPlayerClaim)

        players.remove(victim)  # Remove victim from the game
        if votedOutPlayer != 'skip':
            players.remove(votedOutPlayer)  # Remove voted out player from the game

        # Check if the game is over
        checkGameOver()

def werewolfVictimSyndicate():
    potVictims = []
    for player in players:
        if isinstance(player, WerewolfRole):
            potVictims.append(player.chooseVictim())
    
    return random.choice(potVictims)

def checkGameOver():
    global gameRunning
    numVillagers = sum(1 for player in players if isinstance(player, VillagerRole))
    numWerewolves = sum(1 for player in players if isinstance(player, WerewolfRole))
    numWitches = sum(1 for player in players if isinstance(player, WitchRole))
    numSeers = sum(1 for player in players if isinstance(player, SeerRole))

    if (numSeers + numWitches + numVillagers <= numWerewolves):
        print("Werewolves win!")
        gameRunning = False
    elif numWerewolves == 0:
        print("Villagers win!")
        gameRunning = False

if __name__ == "__main__":
    game()
