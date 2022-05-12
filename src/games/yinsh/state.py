from typing import Optional

from games.yinsh.action import YinshAction
from games.yinsh.result import YinshResult
from games.state import State


class bcolors:
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    cyan = '\033[36m'
    pink = '\033[35m'
    yellow = '\033[33m'
    black = '\033[30m'
    white = '\033[1;97m'
    grey = '\033[1;37m'
    BOLD = '\033[;1m'
    RESET = '\033[0m'


class YinshState(State):
    EMPTY_CELL = -1

    def __init__(self):
        super().__init__()

        """
        the grid
        """
        self.__grid = [
            [-1, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1],
            [-1, -1, -1, 0, -1, 0, -1, 0, -1, -1, -1],
            [-1, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1],
            [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
            [-1, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1],
            [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
            [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
            [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
            [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
            [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
            [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
            [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
            [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
            [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
            [-1, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1],
            [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
            [-1, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1],
            [-1, -1, -1, 0, -1, 0, -1, 0, -1, -1, -1],
            [-1, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1],
        ]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 2

        """
        the index of the current acting player
        """
        self.__acting_player = 1

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

        self.duplaJogada = False

        self.lastActionPos = tuple()

        self.jogadaInvalida = False
        #aqui
    def __check_winner(self, player):
        """# check for 4 up and down
        for row in range(0, 19):
            for col in range(0, 11):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, 19):
            for col in range(0, 11 - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, 19 - 3):
            for col in range(0, 11 - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True
"""
        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: YinshAction) -> bool:
        col = action.get_col()
        row = action.get_row()

        if col < 0 or col > 10:
            return False

        if row < 0 or row > 18:
            return False

        # full column
        if self.__grid[row][col] == YinshState.EMPTY_CELL:
            return False
        return True

    def update(self, action: YinshAction):
        col = action.get_col()
        print(f"col: {col}")
        row = action.get_row()
        print(f"row: {row}")

        if len(self.lastActionPos) == 2:
            lastCol,lastRow=self.lastActionPos
        value = self.__grid[row][col]
        print(value)
        if value==-1:
            self.jogadaInvalida = True
        else:
            # drop the checker
            if self.duplaJogada:
                if value == 0:
                    self.__grid[row][col] = self.__acting_player
                self.__grid[lastRow][lastCol]+=2
                self.duplaJogada = False
            else:
                if value == 0:
                    self.__grid[row][col] = self.__acting_player
                elif value > 0 and value == self.__acting_player:
                    if value == 1 or value == 2:
                        self.duplaJogada = True
                        self.__grid[row][col] = self.__grid[row][col] + 2
                else:
                    self.__acting_player = 1 if self.__acting_player == 2 else 2

        if not self.duplaJogada and not self.jogadaInvalida:
            # determine if there is a winner
            self.__has_winner = self.__check_winner(self.__acting_player)
            # switch to next player
            self.__acting_player = 1 if self.__acting_player == 2 else 2

            self.__turns_count += 1

        self.lastActionPos = (col,row)

    def __display_cell(self, row, col):

        # 0-Locais de jogo | #1- Jogador A | #2- Jogador B | #3- Peça Selecionada A | #4- Peça Selecionada B |
        ##- Locais permitidos para jogar | #5- Peça fixa do jogador A | #6- Peça fixa do jogador B
        print({
                  0: bcolors.white + '◦' + bcolors.RESET,
                  1: bcolors.blue + '◯' + bcolors.RESET,
                  2: bcolors.red + '◯' + bcolors.RESET,
                  3: bcolors.blue + '◉' + bcolors.RESET,
                  4: bcolors.red + '◉' + bcolors.RESET,
                  # 5: bcolors.green + '◎' + bcolors.RESET,
                  5: bcolors.blue + '●' + bcolors.RESET,
                  6: bcolors.red + '●' + bcolors.RESET,
                  YinshState.EMPTY_CELL: ' '
              }[self.__grid[row][col]], end="")


    def __display_numbers(self):
        print('   ', end="")
        for col in range(0, 11):
            if col < 11:
                print('   ', end="")
            print(col, end="")
        print("")

    def display(self):
        self.__display_numbers()
        # for row in self.__grid:
        #    print(row)
        #    print('-'*100)
        #print(self.jogadaInvalida)
        if self.jogadaInvalida:
            print(bcolors.red+"Jogada Inválida! Jogue Novamente!!"+bcolors.RESET)

        for row in range(0, 19):
            if row < 10:
                print(row, '    ', end="")
            else:
                print(row, '   ', end="")
            for col in range(0, 11):
                self.__display_cell(row, col)
                print('   ', end="")
            print("")

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (11 * 19)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player - 1

    def clone(self):
        cloned_state = YinshState()
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, 19):
            for col in range(0, 11):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[YinshResult]:
        if self.__has_winner:
            return YinshResult.LOOSE if pos == self.__acting_player else YinshResult.WIN
        if self.__is_full():
            return YinshResult.DRAW
        return None

    def get_num_rows(self):
        return 19

    def get_num_cols(self):
        return 11

    def before_results(self):
        pass
