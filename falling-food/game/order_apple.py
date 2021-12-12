from game import constants
from game.order_fruit import OrderFruit

class OrderApple(OrderFruit):
    def __init__(self):
        super().__init__()
        
        self.counter.append('apple')
        self._image = constants.IMAGE_FRUIT2