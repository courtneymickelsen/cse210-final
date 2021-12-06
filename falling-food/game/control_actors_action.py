from game import constants
from game.action import Action
from game.input_service import InputService

from game.point import Point

class ControlActorsAction(Action):
    def __init__(self):
        super().__init__()

    def execute(self, cast):
        paddle = cast["paddle"][0]

        # get position
        position = paddle.get_position()
        x = position.get_x()
        y = position.get_y()
        
        if x < (constants.MAX_X - constants.PADDLE_WIDTH) and InputService().is_right_pressed():
            x += constants.PADDLE_SPEED

        if x > 0 and InputService().is_left_pressed():
            x -= constants.PADDLE_SPEED
    
        paddle.set_position(Point(x, y))