from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    def __init__(self):
        super().__init__()

    def execute(self, cast):    
        for group in cast.values():
            for actor in group:
                velocity = actor.get_velocity()
                dx = velocity.get_x()
                dy = velocity.get_y()

                position = actor.get_position()
                x = position.get_x()
                y = position.get_y()

                new_x = x + dx
                new_y = y + dy

                actor.set_position(Point(new_x, new_y))