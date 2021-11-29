from game.action import Action
from game.input_service import InputService
from game.paddle import Paddle

class ControlActorsAction(Action):
    def __init__(self):
        pass

    def execute(self, cast):
        # value = cast.get("paddle")
        
        direction = InputService.get_direction()
        # if direction is left
            # move left
        # if direction is right:
            # move right
        print(direction)

