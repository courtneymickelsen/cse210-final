from game.actor import Actor
from game import constants

class Brick(Actor):
    def __init__(self):
        super().__init__()
        
        self._image = constants.IMAGE_BRICK
        self._width = constants.BRICK_WIDTH
        self._height = constants.BRICK_HEIGHT