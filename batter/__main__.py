import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.brick import Brick
from game.ball import Ball
from game.move_actors_action import MoveActorsAction
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.handle_collisions_action import HandleCollisionsAction
from game.end_game import EndGame
from game.end_message import EndMessage


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    for x in range(constants.BRICK_SPACE, constants.MAX_X, constants.BRICK_WIDTH + constants.BRICK_SPACE):
        for y in range(constants.BRICK_SPACE, 160, constants.BRICK_HEIGHT + constants.BRICK_SPACE):
            brick = Brick()
            brick.set_position(Point(x, y))
            cast["bricks"].append(brick)


    cast["ball"] = []
    ball = Ball()
    ball.set_position(Point(random.randint(100, 700), random.randint(300, 600)))
    cast["ball"].append(ball)

    cast["paddle"] = []
    paddle = Paddle()
    cast["paddle"].append(paddle)

    cast["end_message"] = []
    end_message = EndMessage()
    end_message.set_position(Point(10000, 400))
    cast["end_message"].append(end_message)
    
    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    handle_collisions_action = HandleCollisionsAction()
    end_game = EndGame()

    script["input"] = [control_actors_action]
    script["update"] = [handle_off_screen_action, move_actors_action, handle_collisions_action, end_game,]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
