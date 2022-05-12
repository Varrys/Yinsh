from random import randint

from games.yinsh.action import YinshAction
from games.yinsh.player import YinshPlayer
from games.yinsh.state import YinshState
from games.state import State


class RandomYinshPlayer(YinshPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: YinshState):
        return YinshAction(randint(0,18),randint(0,10))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
