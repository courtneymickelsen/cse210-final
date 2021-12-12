from game.action import Action
from game.basket import Basket
from game.order import Order
from game.director import Director

class CheckOrder(Action):
    def __init__(self):
        super().__init__()
        self.is_order_correct = False

    def execute(self, cast):
        order_names = Order().get_name_list()
        basket_names = Basket().get_name_list()

        for i in order_names:
            for j in basket_names:
                if i == j:
                    # basket_names.pop(i)
                    order_names.pop(j)

        # len(basket_names) == 0 and
        if len(order_names) == 0:
            self.is_order_correct = True
        else:
            self.is_order_correct = False

        if self.is_order_correct == True:
            Director._keep_playing = False