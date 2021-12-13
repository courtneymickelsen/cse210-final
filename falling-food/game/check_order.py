from game.action import Action
from game.basket import Basket
from game.basket_fruit import BasketFruit
from game.order import Order
from game.order_fruit import OrderFruit
from game.director import Director

class CheckOrder(Action):
    def __init__(self):
        super().__init__()
        self.is_order_correct = False

    def execute(self, cast):
        order_names = Order().get_items()
        basket_names = Basket().get_items()
        for i in order_names:
            for j in basket_names:
                if i == j:
                    basket_names.pop(i)
                    order_names.pop(i)

        print(f'basket fruit: {BasketFruit.counter}\norder fruit: {OrderFruit.counter}')
        
        if BasketFruit.counter == OrderFruit.counter:
            self.is_order_correct = True

        if self.is_order_correct:
            print("order correct")
            Director()._keep_playing = False