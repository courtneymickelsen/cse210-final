from game import constants
from game.basket_fruit import BasketFruit

class BasketApple(BasketFruit):
    def __init__(self):
        super().__init__()

        self.counter.append('apple')
        self._image = constants.IMAGE_FRUIT2