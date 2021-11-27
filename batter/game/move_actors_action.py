from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    
    def execute(self, cast):
        for group in cast:
            
            position = cast[group].get_velocity() + cast[group].get_position()
            cast[group]._set_position(position)