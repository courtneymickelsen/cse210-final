from game.fruit import Fruit
from game import constants

class Mango(Fruit):
    def __init__(self):
        super().__init__()

        self._image = constants.IMAGE_MANGO