from game import constants
from game.basket_fruit import BasketFruit

class BasketOrange(BasketFruit):
    def __init__(self):
        super().__init__()

        self.counter.append('orange')
        self._image = constants.IMAGE_FRUIT3