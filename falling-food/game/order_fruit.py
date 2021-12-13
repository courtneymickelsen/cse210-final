from game.fruit import Fruit
from game.point import Point

class OrderFruit(Fruit):
    counter = []
    
    def __init__(self):
        super().__init__()

        self._velocity = Point(0, 0)

        print(self.counter)
