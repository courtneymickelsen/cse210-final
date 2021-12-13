from game.actor import Actor
from game import constants
from game.point import Point

import random

class Fruit(Actor):
    def __init__(self):
        super().__init__()

        self._image = constants.IMAGE_PEAR
        self._width = constants.FRUIT_WIDTH
        self._height = constants.FRUIT_HEIGHT
        self._velocity = Point(0, random.randint(4, 7))
        self._name = 'fruit'

    def get_name(self, item):
        # if item is Apple():
        #     self._name = 'apple' 
        # elif item == Mango():
        #     self._name = 'mango'
        # elif item == Pear():
        #     self._name = 'pear'
        if item == Fruit():
            self._name = 'fruit'

        return self._name