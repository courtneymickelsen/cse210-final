from game import constants
from game.order_fruit import OrderFruit

class OrderOrange(OrderFruit):
    def __init__(self):
        super().__init__()
        
        self.counter.append('orange')
        self._image = constants.IMAGE_FRUIT3