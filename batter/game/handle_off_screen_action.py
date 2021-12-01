from game.action import Action
from game import constants
from game.point import Point

class HandleOffScreenAction(Action):
    def __init__(self):
        super().__init__()

    def execute(self, cast):
        # find ball in cast
        ball = cast["ball"][0]

        # find the position of the ball
        position = ball.get_position()
        x = position.get_x()
        y = position.get_y()

        # find the velocity of the ball
        velocity = ball.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y()

        if (x < 0) or (x > constants.MAX_X):
            new_dx = (dx * -1)
            ball.set_velocity(Point(new_dx, dy))
            
        # elif x > constants.MAX_X:
        #     new_dx = dx * -1
        #     ball.set_velocity(Point(new_dx, dy))

        if y < 0:
            new_dy = dy * -1
            ball.set_velocity(Point(dx, new_dy))