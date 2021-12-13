from game.check_order import CheckOrder
from game.action import Action
from game.point import Point
import random

class PileFruit(Action):
    def __init__(self):
        super().__init__()

    def execute(self,  cast):
        if self.is_order_correct:
            for fruit in cast["fruit"]:
                position = fruit.get_position()
                fruit_y = position.get_y()
                if fruit_y == random.randint(5, 570):
                    fruit.set_velocity(Point(0, 0))