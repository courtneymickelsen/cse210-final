from game import constants
from game.basket_fruit import BasketFruit

class BasketMango(BasketFruit):
    def __init__(self):
        super().__init__()

        self.counter.append('mango')
        self._image = constants.IMAGE_MANGO