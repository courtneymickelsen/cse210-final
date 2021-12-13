from game import constants
from game.order_fruit import OrderFruit

class OrderMango(OrderFruit):
    def __init__(self):
        super().__init__()

        self._image = constants.IMAGE_MANGO