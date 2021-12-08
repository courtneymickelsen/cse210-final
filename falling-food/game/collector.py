from game.actor import Actor
from game import constants
from game.point import Point

class Collector(Actor):
    def __init__(self):
        super().__init__()

        self._height = constants.COLLECTOR_HEIGHT
        self._width = constants.COLLECTOR_WIDTH
        self._image = constants.IMAGE_COLLECTOR
        self._position = Point(370, 570)