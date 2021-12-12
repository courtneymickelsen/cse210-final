from game.fruit import Fruit
from game.point import Point

class OrderFruit(Fruit):
    def __init__(self):
        super().__init__()

        self._velocity = Point(0, 0)
