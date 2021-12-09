from game.actor import Actor
from game.point import Point
from game import constants

class Basket(Actor):
    def __init__(self):
        super().__init__()

        self._image = constants.IMAGE_BASKET
        self._velocity = Point(0, 0)
        self._position = Point(10, 570)