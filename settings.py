# Screen dimensions


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 25
SCREEN_TITLE = "Tetris"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

# Tetromino shapes
SHAPES = [
    [
        [".....", ".....", ".....", "OOOO.", "....."],
        [".....", "..O..", "..O..", "..O..", "..O.."],
    ],
    [
        [".....", ".....", "..O..", ".OOO.", "....."],
        [".....", "..O..", ".OO..", "..O..", "....."],
        [".....", ".....", ".OOO.", "..O..", "....."],
        [".....", "..O..", "..OO.", "..O..", "....."],
    ],
    [
        [".....", ".....", "..OO.", ".OO..", "....."],
        [".....", ".....", ".OO..", "..OO.", "....."],
        [".....", ".O...", ".OO..", "..O..", "....."],
        [".....", "..O..", ".OO..", ".O...", "....."],
    ],
    [
        [".....", "..O..", "..O.", "..OO.", "....."],
        [".....", "...O.", ".OOO.", ".....", "....."],
        [".....", ".OO..", "..O..", "..O..", "....."],
        [".....", ".....", ".OOO.", ".O...", "....."],
    ],
]
