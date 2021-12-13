from game.fruit import Fruit
from game import constants

class Watermelon(Fruit):
    def __init__(self):
        super().__init__()

        self._image = constants.IMAGE_WATERMELON