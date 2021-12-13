from game.action import Action
from game.director import Director
from game.point import Point
from game import constants
import time

class EndGame(Action):
    def __init__(self):
        self._end_game = False

    def execute(self, cast):
        end_message = cast["end_message"][0]
        ball = cast["ball"][0]
        position = ball.get_position()
        y = position.get_y()

        if y > constants.MAX_Y + 10:
            end_message.set_text('You Lose! Try again.')
            end_message.set_position(Point(350, 300))
            self._end_game = True

        elif len(cast["bricks"]) == 0:
            end_message.set_position(Point(400, 300))
            self._end_game = True

        if self._end_game:
            paddle = cast["paddle"][0]
            paddle.set_width(1000)
            paddle.set_position(Point(0, constants.PADDLE_Y))
            
            # I know this isn't the best way to end the game, but I can't find a better way
            Director._keep_playing = False