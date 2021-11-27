from game.action import Action

class MoveActorsAction(Action):
    
    def execute(self, cast):
        for group in cast:
            for actor in group:
                position = (cast[group][actor]._velocity) + (cast[group][actor]._position)
                cast[group][actor]._set_position(position)
                # actor +=1