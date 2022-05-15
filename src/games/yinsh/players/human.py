from games.yinsh.action import YinshAction
from games.yinsh.player import YinshPlayer
from games.yinsh.state import YinshState


class bcolors:
    red = '\033[31m'
    blue = '\033[34m'
    RESET = '\033[0m'


class HumanYinshPlayer(YinshPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: YinshState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                col = int(input(
                    f"Player {bcolors.blue + 'Blue' + bcolors.RESET if state.get_acting_player() == 0 else bcolors.red + 'Red' + bcolors.RESET}, choose a column: "))
                row = int(input(
                    f"Player {bcolors.blue + 'Blue' + bcolors.RESET if state.get_acting_player() == 0 else bcolors.red + 'Red' + bcolors.RESET}, choose a row: "))
                return YinshAction(col, row)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: YinshState):
        # ignore
        pass

    def event_end_game(self, final_state: YinshState):
        # ignore
        pass
