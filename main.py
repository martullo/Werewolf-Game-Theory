from villager_role import VillagerRole
from werewolf_role import WerewolfRole
from seer_role import SeerRole
from witch_role import WitchRole

gameRunning = True

players = [
    VillagerRole(numPlayers=6),
    WerewolfRole(numPlayers=3),
    SeerRole(numPlayers=1),
    WitchRole(numPlayers=1)
]

# Notes:
# - We decided on an initial day phase. What exactly does it entail? Just a
#   discussion but no voting?
# - We said we'll handle the players of a role as one entity. If we do that, we can't
#   have multiple strategies for the same role in one simulation.


while gameRunning:
    # --- Night Phase
    print("Night Phase")
    # Werewolfs choose victim
    victim = werewolfsChooseVictim()
    print(f"Werewolves chose victim: {victim}")

    # Seer(s) choose player to check
    playerToCheck = seersChoosePlayerToCheck()
    print(f"Seer(s) chose player to check: {playerToCheck}")
    # Seer(s) update claims


    # Witch sees killed player and chooses to save them or poison another player


    # --- Day Phase
    print("Day Phase")

    # Game reveals who died during the night

    # --- --- Discussion Phase
    print("§ Discussion")

    # Player(s) killed this night get to claim all players role
    
    # Alive players make claims about all roles

    # --- --- Voting Phase
    print("§ Voting")
    # Alive players vote to kill player or skip (tie is skip)

    # Voted out player is announced

    # Voted out player gets to claim all players role


def werewolfsChooseVictim():
    for player in players:
        if isinstance(player, WerewolfRole):
            return player.chooseVictim()

def seersChoosePlayerToCheck():
    for player in players:
        if isinstance(player, SeerRole):
            return player.choosePlayerToCheck()


if __name__ == "__main__":
    pass