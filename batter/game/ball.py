from game.actor import Actor
from game import constants
from game.point import Point

class Ball(Actor):
    def __init__(self):
        super().__init__()

        self._image = constants.IMAGE_BALL
        self._width = constants.BALL_WIDTH
        self._height = constants.BALL_HEIGHT
        self._velocity = Point(constants.BALL_DX, constants.BALL_DY)
