
import pygame
import math
import random
import id, color

COLUMNS = 8
ROWS = 7

class Board:

    SQUARE_SIZE = 64

    def __init__(self, game):
        self.game = game
        self.board = self.create_board()
        self.surface = pygame.Surface((Board.SQUARE_SIZE*COLUMNS, Board.SQUARE_SIZE*ROWS))
        self.tempSurface = pygame.Surface((Board.SQUARE_SIZE*COLUMNS, Board.SQUARE_SIZE*ROWS), pygame.SRCALPHA)
        self.highlightSurface = pygame.Surface((Board.SQUARE_SIZE*COLUMNS, Board.SQUARE_SIZE*ROWS), pygame.SRCALPHA)
        self.tempHighlightSurface = pygame.Surface((Board.SQUARE_SIZE*COLUMNS, Board.SQUARE_SIZE*ROWS), pygame.SRCALPHA)

        self.highlightImage = pygame.Surface((Board.SQUARE_SIZE, Board.SQUARE_SIZE), pygame.SRCALPHA)
        for i in range(10):
            pygame.draw.rect(self.highlightImage, (255, 255, 255, 2*(10-i)**2), (0, i*0.2*Board.SQUARE_SIZE/10, Board.SQUARE_SIZE, 0.2*Board.SQUARE_SIZE/10+1))

        self.playerSquares = [(0, ROWS - 1)]
        self.opponentSquares = [(COLUMNS - 1, 0)]

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
        self.animation = 10
        for column in range(COLUMNS):
            for row in range(ROWS):
                pygame.draw.rect(self.tempSurface, color.COLORS[self.board[column][row]] + (100,),
                                (column*Board.SQUARE_SIZE, row*Board.SQUARE_SIZE, Board.SQUARE_SIZE, Board.SQUARE_SIZE))

    def draw(self):
        if self.animation > 0:
            self.animation -= 1
            self.surface.blit(self.tempSurface, (0, 0))
        
        self.game.surface.blit(self.surface, (self.game.WIDTH/2 - Board.SQUARE_SIZE*COLUMNS/2, self.game.HEIGHT/2 - Board.SQUARE_SIZE*ROWS/2))
        #self.game.surface.blit(self.highlightImage, (0, 0))

    def getPlayer(self) -> int:
        return self.board[0][-1]

    def getOpponent(self) -> int:
        return self.board[-1][0]
    
    def changeColor(self, new_color, squares):
        def check(column, row):
            return self.board[column][row] == new_color and (column, row) not in squares

        for square in squares:
            column, row = square

            self.board[column][row] = new_color

            if column < COLUMNS - 1 and check(column + 1, row):
                squares.append((column + 1, row))
            if column > 0 and check(column - 1, row):
                squares.append((column - 1, row))
            if row < ROWS - 1 and check(column, row + 1):
                squares.append((column, row + 1))
            if row > 0 and check(column, row - 1):
                squares.append((column, row - 1))


