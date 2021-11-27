from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    def __init__(self):
        pass

    # def execute(self, cast):
    #     for group in cast:
    #         for actor in group:
    #             # HELP: I can't access the actual actors in the dictionary
    #             # They're in the dictionary as storage locations
    #             new_position = cast[group][actor].get_velocity() + cast[group][actor].get_position()
    #             cast[group][actor]._set_position(new_position)