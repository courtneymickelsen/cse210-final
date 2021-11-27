from game.action import Action
from game.input_service import InputService

class ControlActorsAction(Action):
    def __init__(self):
        pass

    def execute(self):
        direction = InputService.get_direction()
        # finish this!
        print(direction)
