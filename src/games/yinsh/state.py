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

        # The grid
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

        self.lastActionPos = (8, 8)

    def __check_winner(self, player):
        # check for 4 up and down
        bolaPlayer = 5 if player == 1 else 6
        for row in range(0, 19):
            for col in range(0, 11):
                if self.__grid[row][col] == bolaPlayer and \
                        self.__grid[row + 2][col] == bolaPlayer and \
                        self.__grid[row + 4][col] == bolaPlayer and \
                        self.__grid[row + 6][col] == bolaPlayer and \
                        self.__grid[row + 8][col] == bolaPlayer:
                    print("O player", bcolors.blue + "Blue" + bcolors.RESET if bolaPlayer == 5 else bcolors.red + 'Red' + bcolors.RESET, "ganhou ")
                    return True

        # check upward diagonal
        for row in range(3, 19):
            for col in range(0, 11 - 3):
                if self.__grid[row][col] == bolaPlayer and \
                        self.__grid[row - 1][col + 1] == bolaPlayer and \
                        self.__grid[row - 2][col + 2] == bolaPlayer and \
                        self.__grid[row - 3][col + 3] == bolaPlayer and \
                        self.__grid[row - 4][col + 4] == bolaPlayer:
                    print("O player", bcolors.blue + "Blue" + bcolors.RESET if bolaPlayer == 5 else bcolors.red + 'Red' + bcolors.RESET, "ganhou ")
                    return True

        # check downward diagonal
        for row in range(0, 19 - 3):
            for col in range(0, 11 - 3):
                if self.__grid[row][col] == bolaPlayer and \
                        self.__grid[row + 1][col + 1] == bolaPlayer and \
                        self.__grid[row + 2][col + 2] == bolaPlayer and \
                        self.__grid[row + 3][col + 3] == bolaPlayer and \
                        self.__grid[row + 4][col + 4] == bolaPlayer:
                    print("O player", bcolors.blue + "Blue" + bcolors.RESET if bolaPlayer == 5 else bcolors.red + 'Red' + bcolors.RESET, "ganhou ")
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: YinshAction) -> bool:
        col = action.get_col()
        row = action.get_row()
        value = self.__grid[row][col]

        if col < 0 or col > 10:
            return False

        if row < 0 or row > 18:
            return False

        if value == YinshState.EMPTY_CELL:
            return False

        # Impede de jogar onde existem peças, até terminar de colocar as 5º primeiras
        if (value == 1 or value == 2) and self.__turns_count < 12:
            return False

        # Impende colocar uma peça numa cel vazia depois das 5/10 jogadas
        if value == 0 and self.__turns_count > 11 and not self.duplaJogada:
            return False

        # Não deixa jogar onde já há jogadas e se tem uma peça selecionada
        if value > 0 and self.duplaJogada:
            return False

        if self.__turns_count >= 12 and self.duplaJogada:
            # Não deixa jogar na horizontal
            lastRow, lastCol = self.lastActionPos
            if row == lastRow:
                return False
            rowDiff = abs(lastRow - row)
            # Não deixa jogar entre as verticais e as diagonais
            if row != lastRow and col not in [lastCol + rowDiff, lastCol - rowDiff, lastCol]:
                return False

            # Este pequeno codigo não deixa jogar numa posição se tiver peças 1/2 nessa vertical
            if col == lastCol:
                if row > lastRow:
                    for i in range(lastRow + 1, row + 1):
                        valor = self.__grid[i][col]
                        if valor != self.__acting_player and 0 < valor < 5:
                            return False
                        # Verifica se existe uma peça 5/6 depois verifica se é onde quero jogar e se não for verifica se na linha a seguir existe a peça 5/6
                        elif valor in [5, 6] and (i + 2) != row and self.__grid[i + 2][col] not in [5, 6]:
                            return False
                else:
                    for i in reversed(range(row, lastRow)):
                        valor = self.__grid[i][col]
                        if valor != self.__acting_player and 0 < valor < 5:
                            return False
                        elif valor in [5, 6] and (i - 2) != row and self.__grid[i - 2][col] not in [5, 6]:
                            return False

            # Este pequeno codigo não deixa jogar numa posição se tiver peças 1/2 nessa diagonal
            if row > lastRow and col != lastCol:
                for i in range(lastRow + 1, row + 1, ):
                    rowDiff = abs(lastRow - i)
                    playCol = lastCol + rowDiff if (lastCol - col) < 0 else lastCol - rowDiff
                    checkCol = playCol + 1 if (lastCol - col) < 0 else playCol - 1
                    valor = self.__grid[i][playCol]
                    if valor != self.__acting_player and 0 < valor < 5:
                        return False
                    elif valor in [5, 6] and (i + 1) != row and self.__grid[i + 1][checkCol] not in [5, 6]:
                        return False

            elif row < lastRow and col != lastCol:
                for i in reversed(range(row, lastRow, )):
                    rowDiff = abs(lastRow - i)
                    playCol = lastCol + rowDiff if (lastCol - col) < 0 else lastCol - rowDiff
                    checkCol = playCol + 1 if (lastCol - col) < 0 else playCol - 1
                    valor = self.__grid[i][playCol]
                    if valor != self.__acting_player and 0 < valor < 5:
                        return False
                    elif valor in [5, 6] and (i - 1) != row and self.__grid[i - 1][checkCol] not in [5, 6]:
                        return False
        return True

    def update(self, action: YinshAction):
        col = action.get_col()
        row = action.get_row()

        if len(self.lastActionPos) == 2:
            lastRow, lastCol = self.lastActionPos
        value = self.__grid[row][col]

        # drop the checker
        if self.duplaJogada:
            self.__grid[row][col] = self.__acting_player
            self.__grid[lastRow][lastCol] += 2
            self.duplaJogada = False
            if col == lastCol:
                if row > lastRow:
                    for i in range(lastRow + 1, row + 1):
                        valor = self.__grid[i][col]
                        if valor == 5:
                            self.__grid[i][col] = 6
                        elif valor == 6:
                            self.__grid[i][col] = 5
                else:
                    for i in reversed(range(row, lastRow)):
                        valor = self.__grid[i][col]
                        if valor == 5:
                            self.__grid[i][col] = 6
                        elif valor == 6:
                            self.__grid[i][col] = 5

            if row > lastRow and col != lastCol:
                for i in range(lastRow + 1, row + 1, ):
                    rowDiff = abs(lastRow - i)
                    playCol = lastCol + rowDiff if (lastCol - col) < 0 else lastCol - rowDiff
                    valor = self.__grid[i][playCol]
                    if valor == 5:
                        self.__grid[i][playCol] = 6
                    elif valor == 6:
                        self.__grid[i][playCol] = 5
            elif row < lastRow and col != lastCol:
                for i in reversed(range(row, lastRow, )):
                    rowDiff = abs(lastRow - i)
                    playCol = lastCol + rowDiff if (lastCol - col) < 0 else lastCol - rowDiff
                    valor = self.__grid[i][playCol]
                    if valor == 5:
                        self.__grid[i][playCol] = 6
                    elif valor == 6:
                        self.__grid[i][playCol] = 5
        else:
            if value == 0:
                self.__grid[row][col] = self.__acting_player
            elif value > 0 and value == self.__acting_player:
                if value == 1 or value == 2:
                    self.duplaJogada = True
                    self.__grid[row][col] = self.__grid[row][col] + 2
            else:
                self.__acting_player = 1 if self.__acting_player == 2 else 2

        if not self.duplaJogada:
            # determine if there is a winner
            self.__has_winner = self.__check_winner(self.__acting_player)
            # switch to next player
            self.__acting_player = 1 if self.__acting_player == 2 else 2

            self.__turns_count += 1

        self.lastActionPos = (row, col)

    def __display_cell(self, row, col):

        # 0-Locais de jogo | #1- Jogador azul | #2- Jogador vermelho | #3- Peça Selecionada azul | #4- Peça Selecionada vermelha
        # 5- Peça fixa do jogador azul | #6- Peça fixa do jogador vermelha
        print({
                  0: bcolors.white + '◦' + bcolors.RESET,
                  1: bcolors.blue + '◯' + bcolors.RESET,
                  2: bcolors.red + '◯' + bcolors.RESET,
                  3: bcolors.blue + '◉' + bcolors.RESET,
                  4: bcolors.red + '◉' + bcolors.RESET,
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
