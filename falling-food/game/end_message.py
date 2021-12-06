from game.actor import Actor
from game.point import Point
from game import constants

class EndMessage(Actor):
    def __init__(self):
        super().__init__()
        self._text = ""
        self._width = 400
        self._height = 100
        self._text = "You win!"
        # self._velocity = Point(0, 0)
        