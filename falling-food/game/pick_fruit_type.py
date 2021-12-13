from game.order_apple import OrderApple
from game.order_mango import OrderMango
from game.order_pear import OrderPear
from game.order_watermelon import OrderWatermelon
from game.action import Action
import random

class PickFruitType(Action):
    def __init__(self):
        self.order_fruit_types = [OrderApple(), OrderMango(), OrderPear(), OrderWatermelon()]
        self.fruit_type = ''

    def execute(self):
        self.fruit_type = random.choice(self.order_fruit_types)
        return self.fruit_type