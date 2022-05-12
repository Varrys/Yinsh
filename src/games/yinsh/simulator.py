from games.yinsh.player import YinshPlayer
from games.yinsh.state import YinshState
from games.game_simulator import GameSimulator


class YinshSimulator(GameSimulator):

    def __init__(self, player1: YinshPlayer, player2: YinshPlayer):
        super(YinshSimulator, self).__init__([player1, player2])


    def init_game(self):
        return YinshState()

    def before_end_game(self, state: YinshState):
        # ignored for this simulator
        pass

    def end_game(self, state: YinshState):
        # ignored for this simulator
        pass
