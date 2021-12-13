from game.action import Action
from game.basket import Basket
from game.basket_fruit import BasketFruit
from game.order import Order
from game.order_fruit import OrderFruit
from game.director import Director
from game.point import Point
from game.fruit import Fruit
from game.end_game import EndGame
import random

class CheckOrder(Action):
    def __init__(self):
        super().__init__()
        self.is_order_correct = False

    def execute(self, cast):
        # order_names = Order().get_items()
        # basket_names = Basket().get_items()

        # for i in order_names:
        #     for j in basket_names:
        #         if i == j:
        #             basket_names.pop(i)
        #             order_names.pop(i)

        print(f'basket fruit: {BasketFruit.counter}\norder fruit: {OrderFruit.counter}')
        self.check_win(cast)
        self.check_lose(cast)
    
    def check_lose(self, cast):
        basket_length = len(BasketFruit.counter)
        order_length = len(OrderFruit.counter)
        
        for i in range(basket_length):
            if basket_length <= order_length:
                if BasketFruit.counter[i] != OrderFruit.counter[i]:
                    end_message = cast["end_message"][0]
                    end_message.set_text('Wrong Order! Try Again.')
                    end_message.set_position(Point(310, 300))
                    # EndGame().execute(cast)

    def check_win(self, cast):
        if BasketFruit.counter == OrderFruit.counter:
            self.is_order_correct = True

        if self.is_order_correct:
            end_message = cast["end_message"][0]
            end_message.set_position(Point(370, 300))
            EndGame().execute(cast)