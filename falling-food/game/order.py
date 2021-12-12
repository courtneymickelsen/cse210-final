from game.fruit import Fruit

class Order():
    def __init__(self):
        self._items = []
        self._name = ''
        self._name_list = []

    def get_items(self):
        return self._items

    def add_item(self, item):
        self._items.append(item)

    def _add_name(self, item):
        name = Fruit.get_name(item)
        self._name_list.append(name)

    def get_name_list(self):
        self._name_list = []

        for item in self._items:
            self._add_name(item)
        
        return self._name_list
