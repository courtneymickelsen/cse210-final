from game.action import Action
from game.physics_service import PhysicsService
from game.point import Point
from game.audio_service import AudioService
from game import constants

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

        if PhysicsService().is_collision(collector, fruit):
            # ToDo: make the fruit move with the guy
            AudioService().play_sound(constants.SOUND_BOUNCE)

        for fruit in cast["fruit"]:
            if PhysicsService().is_collision(fruit, basket):
                index = cast["fruit"].index(fruit)
                cast["fruit"].pop(index)
                # fruit.set_position(Point(basket location))
                fruit.set_velocity(Point(0, 0))
                AudioService().play_sound(constants.SOUND_BOUNCE)