from game import constants
from game.basket_fruit import BasketFruit

class BasketPear(BasketFruit):
    def __init__(self):
        super().__init__()

        self.counter.append('pear')
        self._image = constants.IMAGE_PEAR