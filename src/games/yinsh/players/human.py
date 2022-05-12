from games.yinsh.action import YinshAction
from games.yinsh.player import YinshPlayer
from games.yinsh.state import YinshState


class HumanYinshPlayer(YinshPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: YinshState):
        state.display()
        #AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        while True:
            # noinspection PyBroadException
            try:
                col = int(input(f"Player {state.get_acting_player()}, choose a column: "))
                row = int(input(f"Player {state.get_acting_player()}, choose a row: "))
                return YinshAction(col,row)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: YinshState):
        # ignore
        pass

    def event_end_game(self, final_state: YinshState):
        # ignore
        pass
