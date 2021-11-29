from game.action import Action

class HandleOffScreenAction(Action):
    def __init__(self):
        pass

    def execute(self, cast):
        # find ball in cast
        # find position of the ball
        # if position(x) <0 
            # add 1 to it's velocity(x)
        # elif position(x) > MAX _X
            # subtract 1 from velocity(x)
        # if position(y) < 0
            # add 1 to velocity(y)
        pass