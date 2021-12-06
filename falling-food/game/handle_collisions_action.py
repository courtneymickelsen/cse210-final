from game.action import Action
from game.physics_service import PhysicsService
from game.point import Point
from game.audio_service import AudioService
from game import constants

class HandleCollisionsAction(Action):
    def __init__(self):
        super().__init__()

    def execute(self, cast):
        ball = cast["ball"][0]
        ball_velocity = ball.get_velocity()
        dx = ball_velocity.get_x()
        dy = ball_velocity.get_y()
        
        paddle = cast["paddle"][0]

        if PhysicsService().is_collision(paddle, ball):
            new_dy = -abs(dy)
            ball.set_velocity(Point(dx, new_dy))
            AudioService().play_sound(constants.SOUND_BOUNCE)

        for brick in cast["bricks"]:
            if PhysicsService().is_collision(brick, ball):
                AudioService().play_sound(constants.SOUND_BOUNCE)
                index = cast["bricks"].index(brick)
                cast["bricks"].pop(index)
                new_dy = dy * -1
                ball.set_velocity(Point(dx, new_dy))
