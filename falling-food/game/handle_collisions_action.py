from game.action import Action
from game.physics_service import PhysicsService
from game.point import Point
from game.audio_service import AudioService
from game.fruit import Fruit
from game.control_actors_action import ControlActorsAction
from game import constants
from game.input_service import InputService
import random

class HandleCollisionsAction(Action):
    def __init__(self):
        super().__init__()

    def execute(self, cast):
        fruit = cast["fruit"][0]
        fruit_velocity = fruit.get_velocity()
        fruit_dx = fruit_velocity.get_x()
        fruit_dy = fruit_velocity.get_y()
        
        collector = cast["collector"][0]
        basket = cast["basket"][0]

        for fruit in cast["fruit"]:
            if PhysicsService().is_collision(collector, fruit):
                ControlActorsAction.carry_fruit(collector, fruit)
                AudioService().play_sound(constants.SOUND_BOUNCE)

        for fruit in cast["fruit"]:
            if PhysicsService().is_collision(fruit, basket):
                fruit.set_velocity(Point(0, 0))
                self.drop_fruit(cast, fruit, basket)
                AudioService().play_sound(constants.SOUND_BOUNCE)

    def drop_fruit(self, cast, fruit, basket):
        # index = cast["fruit"].index(fruit)
        # cast["fruit"].pop(index)

        basket_location = basket.get_position()
        basket_x = basket_location.get_x()
        basket_y = basket_location.get_y()

        fruit.set_velocity(Point(0, 0))

        fruit.set_position(Point(basket_x, basket_y))

        # if InputService().is_left_pressed() or InputService().is_right_pressed():
            # fruit.set_position(Point(basket_x, (basket_y - random.randint(3, 8))))
                