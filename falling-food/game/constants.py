import os

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

BACKGROUND_COLOR = COLOR_BLACK

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BASKET = os.path.join(os.getcwd(), "./falling-food/assets/brick-3.png")
IMAGE_COLLECTOR = os.path.join(os.getcwd(), "./falling-food/assets/bat.png")
IMAGE_FRUIT1 = os.path.join(os.getcwd(), "./falling-food/assets/ball.png")
IMAGE_FRUIT2 = os.path.join(os.getcwd(), "./falling-food/assets/ball.png")
IMAGE_FRUIT3 = os.path.join(os.getcwd(), "./falling-food/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./falling-food/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./falling-food/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./falling-food/assets/over.wav")

# BALL_X = MAX_X / 2
# BALL_Y = MAX_Y - 125

FRUIT_DX = 8
FRUIT_DY = 0

COLLECTOR_X = MAX_X / 2
COLLECTOR_Y = MAX_Y - 25

COLLECTOR_SPEED = 15

COLLECTOR_WIDTH = 80
COLLECTOR_HEIGHT = 50

FRUIT_WIDTH = 24
FRUIT_HEIGHT = 24

BASKET_WIDTH = 60
BASKET_HEIGHT = 30