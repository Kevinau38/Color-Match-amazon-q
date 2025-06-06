import pygame

# Game constants
WIDTH, HEIGHT = 500, 550  # Increased height to make room for buttons
GRID_SIZE = 10  # Larger grid for color matching game
TILE_SIZE = WIDTH // GRID_SIZE
FPS = 60
ANIMATION_SPEED = 0.25  # Lower is faster

# UI layout
GRID_AREA_HEIGHT = 500  # Original height for the grid area
BUTTON_AREA_HEIGHT = 50  # Height for the button area

# Color palette - medium brightness colors
COLORS = {
    0: (220, 30, 30),    # Medium Red
    1: (30, 200, 30),    # Medium Green
    2: (30, 30, 220),    # Medium Blue
    3: (220, 220, 30),   # Medium Yellow
    4: (200, 30, 200),   # Medium Magenta
    5: (30, 200, 200),   # Medium Cyan
}

# UI colors
BACKGROUND_COLOR = (50, 50, 50)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Game settings
MAX_MOVES = 20  # Limited moves for more challenge
WINNING_PERCENTAGE = 90  # Percentage of board needed to win