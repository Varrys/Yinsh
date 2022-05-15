from games.yinsh.players.minimax import MinimaxYinshPlayer
from games.yinsh.players.random import RandomYinshPlayer
from games.yinsh.simulator import YinshSimulator
from games.game_simulator import GameSimulator
from src.games.yinsh.players.greedy import GreedyYinshPlayer
from src.games.yinsh.players.human import HumanYinshPlayer


class bcolors:
    green = '\033[32m'
    RESET = '\033[0m'


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"---------------- {bcolors.green + desc + bcolors.RESET} ----------------")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 1

    c4_simulations = [
        # uncomment to play as human
        {
            "name": "Human VS Human",
            "player1": HumanYinshPlayer("Human"),
            "player2": HumanYinshPlayer("Human2")
        },
        # {
        #    "name": "Random VS Human",
        #    "player1": RandomYinshPlayer("Random"),
        #    "player2": HumanYinshPlayer("Human")
        # },
        # {
        #    "name": "Random VS Random2",
        #    "player1": RandomYinshPlayer("Random"),
        #    "player2": RandomYinshPlayer("Random2")
        # }
    ]

    for sim in c4_simulations:
        run_simulation(sim["name"], YinshSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
