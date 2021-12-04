from game.action import Action
from game import constants
from game.director import Director

class EndGame(Action):
    def __init__(self):
        self._did_lose = False

    def execute(self, cast):
        ball = cast["ball"][0]
        position = ball.get_position()
        y = position.get_y()
        if y > constants.MAX_Y:
            self._did_lose = True
        else:
            self._did_lose = False
        
        if self._did_lose:
            Director()._keep_playing = False
