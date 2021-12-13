from game import constants
from game.basket_fruit import BasketFruit

class BasketWatermelon(BasketFruit):
    def __init__(self):
        super().__init__()

        self.counter.append('watermelon')
        self._image = constants.IMAGE_WATERMELON