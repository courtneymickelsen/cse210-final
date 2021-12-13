from game.action import Action
from game.order_apple import OrderApple
from game.order_mango import OrderMango
from game.order_pear import OrderPear
from game.order_watermelon import OrderWatermelon
from game.order_fruit import OrderFruit

class AddToOrder(Action):
    def __init__(self):
        super().__init__()

    def execute(self, cast):
        # something could be wrong here
        order_fruit = cast["order_fruit"]

        for item in order_fruit:
            if isinstance(item, OrderApple):
                OrderFruit.counter.append('apple')

            if isinstance(item, OrderMango):
                OrderFruit.counter.append('mango')

            if isinstance(item, OrderPear):
                OrderFruit.counter.append('pear')

            if isinstance(item, OrderWatermelon):
                OrderFruit.counter.append('watermelon')