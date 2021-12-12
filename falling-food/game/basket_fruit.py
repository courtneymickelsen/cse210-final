from game.fruit import Fruit

class BasketFruit(Fruit):
    counter = []
    
    def __init__(self):
        super().__init__()
