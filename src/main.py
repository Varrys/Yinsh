from games.yinsh.players.random import RandomYinshPlayer
from games.yinsh.simulator import YinshSimulator
from games.game_simulator import GameSimulator
from src.games.yinsh.players.human import HumanYinshPlayer


class bcolors:
    green = '\033[32m'
    RESET = '\033[0m'
    BOLD = '\033[;1m'


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"------------------ {bcolors.green + desc + bcolors.RESET} ------------------")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    global c4_simulations
    print(bcolors.BOLD + "               ESTG IA Yinsh Simulator" + bcolors.RESET)
    num_iterations = 1
    option = 0
    print(bcolors.green + "1-" + bcolors.RESET + " Human vs Human")
    print(bcolors.green + "2-" + bcolors.RESET + " Random vs Human")
    print(bcolors.green + "3-" + bcolors.RESET + " Random vs Random2")
    while option > 3 or option < 1:
        option = int(input("Escolha o tipo de jogo: "))

    if option == 1:
        c4_simulations = [{
            "name": "Human VS Human",
            "player1": HumanYinshPlayer("Human"),
            "player2": HumanYinshPlayer("Human2")
        }]
    if option == 2:
        c4_simulations = [{
            "name": "Random VS Human",
            "player1": RandomYinshPlayer("Random"),
            "player2": HumanYinshPlayer("Human")
        }]
    if option == 3:
        c4_simulations = [{
            "name": "Random VS Random2",
            "player1": RandomYinshPlayer("Random"),
            "player2": RandomYinshPlayer("Random2")
        }]

    for sim in c4_simulations:
        run_simulation(sim["name"], YinshSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
