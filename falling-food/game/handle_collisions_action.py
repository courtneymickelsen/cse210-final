from game.basket import Basket
from game.basket_fruit import BasketFruit
from game.action import Action
from game.order import Order
from game.physics_service import PhysicsService
from game.point import Point
from game.audio_service import AudioService
from game.fruit import Fruit
from game.control_actors_action import ControlActorsAction
from game import constants
from game.input_service import InputService
from game.apple import Apple
from game.orange import Orange
from game.basket_orange import BasketOrange
from game.basket_apple import BasketApple
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
                
                if isinstance(fruit, Apple):
                    bf = BasketApple()

                if isinstance(fruit, Orange):
                    bf = BasketOrange()
                
                bf = BasketFruit()
                self.drop_fruit(fruit, basket)
                AudioService().play_sound(constants.SOUND_BOUNCE)

    def drop_fruit(self, fruit, basket):

        basket_location = basket.get_position()
        basket_x = basket_location.get_x()
        basket_y = basket_location.get_y()

        fruit.set_velocity(Point(0, 0))

        fruit.set_position(Point(-100, -100))