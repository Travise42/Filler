
import pygame
import math
import random
import id, color

COLUMNS = 8
ROWS = 7

class Board:

    SQUARE_SIZE = 64

    def __init__(self):
        self.board = self.create_board()
        self.surface = pygame.Surface((Board.SQUARE_SIZE*COLUMNS, Board.SQUARE_SIZE*ROWS))

        self.refresh()

    def create_board(self) -> list:
        new_board = []

        for _c in range(COLUMNS):
            old_square = -1
            new_column = []
            for _r in range(ROWS):
                options = set(range(6))
                options.discard(old_square)
                if len(new_board) > 0: options.discard(new_board[-1][len(new_column)])
                if len(new_board) + 1 == COLUMNS and len(new_column) == 0: options.discard(new_board[0][-1])
                new_square = random.choice(list(options))
                new_column.append(new_square)
                old_square = new_square
            new_board.append(new_column)

        return new_board

    def update(self):
        pass

    def refresh(self):
        for column in range(COLUMNS):
            for row in range(ROWS):
                pygame.draw.rect(self.surface, color.COLORS[self.board[column][row]],
                                 (column*Board.SQUARE_SIZE, row*Board.SQUARE_SIZE, Board.SQUARE_SIZE, Board.SQUARE_SIZE))

    def draw(self, surf, width, height):
        surf.blit(self.surface, (width/2 - Board.SQUARE_SIZE*COLUMNS/2, height/2 - Board.SQUARE_SIZE*ROWS/2))


