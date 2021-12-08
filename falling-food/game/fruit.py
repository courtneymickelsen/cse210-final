from game.actor import Actor
from game import constants
from game.point import Point

class Fruit(Actor):
    def __init__(self):
        super().__init__()

        # self._image = constants.IMAGE_FRUIT
        self._width = constants.FRUIT_WIDTH
        self._height = constants.FRUIT_HEIGHT
        self._velocity = Point(3, -3)

    def grab_fruit(self):
        pass

    def drop_fruit(self):
        pass
    