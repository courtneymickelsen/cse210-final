from game.fruit import Fruit
from game.actor import Actor
from game.point import Point
from game.order import Order
from game import constants

class Basket(Actor):
    def __init__(self):
        super().__init__()

        self._image = constants.IMAGE_BASKET
        self._velocity = Point(0, 0)
        self._position = Point(10, 540)
        self._width = constants.BASKET_WIDTH
        self._height = constants.BASKET_HEIGHT
        self._items = []
        self._name = ''
        self._name_list = []

    def get_items(self):
        return self._items

    def add_item(self, item):
        self._items.append(item)

    def add_name(self, item):
        name = Fruit().get_name(item)
        self._name_list.append(name)

    def get_name_list(self):
        self._name_list = []

        for item in self._items:
            self.add_name()
        
        return self._name_list