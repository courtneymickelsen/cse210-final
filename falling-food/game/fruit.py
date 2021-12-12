from game.actor import Actor
from game import constants
from game.point import Point


class Fruit(Actor):
    def __init__(self):
        super().__init__()

        self._image = constants.IMAGE_FRUIT1
        self._width = constants.FRUIT_WIDTH
        self._height = constants.FRUIT_HEIGHT
        self._velocity = Point(0, 6)
        self._name = 'fruit'

    def get_name(self, item):
        # if item is Apple():
        #     self._name = 'apple' 
        # elif item == Orange():
        #     self._name = 'orange'
        # elif item == Pear():
        #     self._name = 'pear'
        if item == Fruit():
            self._name = 'fruit'

        return self._name