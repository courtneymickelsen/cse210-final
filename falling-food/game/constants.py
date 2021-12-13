import os

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (198, 228, 247)

BACKGROUND_COLOR = COLOR_BLUE

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BASKET = os.path.join(os.getcwd(), "./falling-food/assets/basket.png")
IMAGE_COLLECTOR = os.path.join(os.getcwd(), "./falling-food/assets/crab.png")
IMAGE_APPLE = os.path.join(os.getcwd(), "./falling-food/assets/apple.png")
IMAGE_MANGO = os.path.join(os.getcwd(), "./falling-food/assets/mango.png")
IMAGE_PEAR = os.path.join(os.getcwd(), "./falling-food/assets/pear.png")
IMAGE_WATERMELON = os.path.join(os.getcwd(), "./falling-food/assets/watermelon.png")

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

COLLECTOR_WIDTH = 58
COLLECTOR_HEIGHT = 58

FRUIT_WIDTH = 24
FRUIT_HEIGHT = 24

BASKET_WIDTH = 58
BASKET_HEIGHT = 58