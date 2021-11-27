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

# TODO: Add imports similar to the following when you create these classes
# from game.paddle import Paddle
# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    cast["bricks"] = []
  
    for x in range(0, constants.MAX_X, constants.BRICK_WIDTH):
        for y in range(0, 160, constants.BRICK_HEIGHT):
            brick = Brick()
            brick.set_position(Point(x, y))
            cast["bricks"].append(brick)


    cast["balls"] = []
    # TODO: Create a ball here and add it to the list

    ball = Ball()
    ball.set_position(Point(400, 400))
    cast["balls"].append(ball)

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    draw_actors_action = DrawActorsAction(output_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = []
    script["update"] = [move_actors_action]
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
