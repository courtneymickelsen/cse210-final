import random
from game.check_order import CheckOrder
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.order_fruit import OrderFruit
from game.fruit import Fruit
from game.move_actors_action import MoveActorsAction
from game.collector import Collector
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.end_game import EndGame
from game.end_message import EndMessage
from game.basket import Basket
from game.order import Order

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["fruit"] = []
    for x in range(100):
        for y in range(100):
            fruit = Fruit()
            fruit.set_position(Point(random.randint(50, 800), random.randint(-2000000, 0)))
            cast["fruit"].append(fruit)

    cast["order_fruit"] = []
    next_x = 100
    for i in range(random.randint(5, 15)):
        order_fruit = OrderFruit()
        order_fruit.set_position(Point(10, next_x))
        Order().add_item(order_fruit)
        cast["order_fruit"].append(order_fruit)
        next_x += 30

    cast["basket"] = []
    basket = Basket()
    cast["basket"].append(basket)

    cast["collector"] = []
    collector= Collector()
    cast["collector"].append(collector)

    cast["end_message"] = []
    end_message = EndMessage()
    end_message.set_position(Point(10000, 400))
    cast["end_message"].append(end_message)
    
    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    end_game = EndGame()
    check_order = CheckOrder()

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, check_order]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
