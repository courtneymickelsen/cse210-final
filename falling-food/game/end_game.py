from game.action import Action
from game.director import Director
from game.point import Point
from game import constants
import time

class EndGame(Action):
    def __init__(self):
        self._end_game = False

    def execute(self, cast):
        for fruit in cast["fruit"]:
            position = fruit.get_position()
            fruit_y = position.get_y()
            velocity = fruit.get_velocity()
            fruit_dy = velocity.get_y()
            fruit_dx = velocity.get_x()

            if fruit_dy > 0 and fruit_y in range(570, 600):
                fruit.set_velocity(Point(fruit_dx, (fruit_dy * -1)))

            if fruit_dy < 0 and fruit_y in range(-25, 0):
                fruit.set_velocity(Point(fruit_dx, (fruit_dy * -1)))