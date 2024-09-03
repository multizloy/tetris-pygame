import sys
import pygame
import random
import settings

pygame.init()


class Tetromino:
    def __init__(self, x, y, shape) -> None:
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(
            settings.COLORS
        )  # You can choose different colors for each shape
        self.rotation = 0


class Tetris:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0  # Add score attribute

    def new_piece(self):
        # choose random shape
        shape = random.choice(settings.SHAPES)
        # return Tetromino object
        return Tetromino(self.width // 2, 0, shape)

    