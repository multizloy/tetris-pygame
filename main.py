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

    def valid_move(self, piece, x, y, rotation):
        # check if the piece can move to the given position
        for i, row in enumerate(
            piece.shape[(piece.rotation + rotation) % len(piece.shape)]
        ):
            for j, cell in enumerate(row):
                try:
                    if cell == "0" and (
                        self.grid[piece.y + i + y][piece.x + j + x] != 0
                    ):
                        return False
                except IndexError:
                    return False

        return True

    def clear_lines(self):
        # clear lines
        lines_cleared = 0
        for i, row in enumerate(self.grid[:-1]):
            if all(cell != 0 for cell in row):
                lines_cleared += 1
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(self.width)])

        return lines_cleared

    def lock_piece(self, piece):
        # lock the piece and create a new piece
        for i, row in enumerate(piece.shape[piece.rotation % len(piece.shape)]):
            for j, cell in enumerate(row):
                if cell == "0":
                    self.grid[piece.y + i][piece.x + j] = piece.color
        # clear the lines and update the score
        lines_cleared = self.clear_lines()
        self.score += lines_cleared * 100  # update the score based on the lines cleared
        # create a new piece
        self.current_piece = self.new_piece()
        # check if the game is over
        if not self.valid_move(self.current_piece, 0, 0, 0):
            self.game_over = True
        return lines_cleared

    def update(self):
        # update the game
        if not self.game_over:
            if self.valid_move(self.current_piece, 0, 1, 0):
                self.current_piece.y += 1
            else:
                self.lock_piece(self.current_piece)

    def draw(self, screen):
        # draw the game
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen,
                        cell,
                        (
                            x * settings.GRID_SIZE,
                            y * settings.GRID_SIZE,
                            settings.GRID_SIZE - 1,
                            settings.GRID_SIZE - 1,
                        ),
                    )

        if self.current_piece:
            for i, row in enumerate(self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]):
                for j,cell in enumerate(row):   
                    if cell == "0":
                        pygame.draw.rect(
                            screen,
                            self.current_piece.color,
                            (
                                (self.current_piece.x + j) * settings.GRID_SIZE,
                                (self.current_piece.y + i) * settings.GRID_SIZE,
                                settings.GRID_SIZE - 1,
                                settings.GRID_SIZE - 1,
                            ),
                        )