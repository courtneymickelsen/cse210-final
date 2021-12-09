from game.actor import Actor
from game import constants
from game.point import Point
import random

class Fruit(Actor):
    def __init__(self):
        super().__init__()

        self._image = constants.IMAGE_FRUIT1
        self._width = constants.FRUIT_WIDTH
        self._height = constants.FRUIT_HEIGHT
        self._velocity = Point(0, 3)

    def grab_fruit(self):
        pass

    def drop_fruit(self):
        pass