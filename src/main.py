from games.yinsh.players.minimax import MinimaxYinshPlayer
from games.yinsh.players.random import RandomYinshPlayer
from games.yinsh.simulator import YinshSimulator
from games.game_simulator import GameSimulator
from src.games.yinsh.players.human import HumanYinshPlayer


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 10

    c4_simulations = [
        # uncomment to play as human
        {
            "name": "Yinsh - Human VS Random",
            "player1": HumanYinshPlayer("Human"),
            "player2": HumanYinshPlayer("Human2.0")
        },
        #{
        #    "name": "Yinsh - Random VS Random",
        #    "player1": RandomYinshPlayer("Random 1"),
        #    "player2": RandomYinshPlayer("Random 2")
        #},
        #{
        #    "name": "Yinsh - Greedy VS Random",
        #    "player1": GreedyYinshPlayer("Greedy"),
        #    "player2": RandomYinshPlayer("Random")
        #},
        #{
        #    "name": "Minimax VS Random",
        #    "player1": MinimaxYinshPlayer("Minimax"),
        #    "player2": RandomYinshPlayer("Random")
        #},
        #{
        #    "name": "Minimax VS Greedy",
        #    "player1": MinimaxYinshPlayer("Minimax"),
        #    "player2": GreedyYinshPlayer("Greedy")
        #}
    ]

    for sim in c4_simulations:
        run_simulation(sim["name"], YinshSimulator(sim["player1"], sim["player2"]), num_iterations)

if __name__ == "__main__":
    main()
