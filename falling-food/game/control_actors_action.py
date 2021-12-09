from game import constants
from game.action import Action
from game.input_service import InputService

from game.point import Point

class ControlActorsAction(Action):
    def __init__(self):
        super().__init__()

    def execute(self, cast):
        collector = cast["collector"][0]

        # get position
        position = collector.get_position()
        x = position.get_x()
        y = position.get_y()
        
        if x < (constants.MAX_X - constants.COLLECTOR_WIDTH) and InputService().is_right_pressed():
            x += constants.COLLECTOR_SPEED

        if x > 0 and InputService().is_left_pressed():
            x -= constants.COLLECTOR_SPEED
    
        collector.set_position(Point(x, y))