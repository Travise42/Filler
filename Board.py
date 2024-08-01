
import pygame
import math
import random
import id, color

class Board:

    SQUARE_SIZE = 64
    COLUMNS = 8
    ROWS = 7

    def __init__(self, game):
        self.game = game
        self.board = self.create_board()
        self.surface = pygame.Surface((Board.SQUARE_SIZE*Board.COLUMNS, Board.SQUARE_SIZE*Board.ROWS))
        self.tempSurface = pygame.Surface((Board.SQUARE_SIZE*Board.COLUMNS, Board.SQUARE_SIZE*Board.ROWS), pygame.SRCALPHA)
        self.highlightSurface = pygame.Surface((Board.SQUARE_SIZE*Board.COLUMNS, Board.SQUARE_SIZE*Board.ROWS), pygame.SRCALPHA)
        self.tempHighlightSurface = pygame.Surface((Board.SQUARE_SIZE*Board.COLUMNS, Board.SQUARE_SIZE*Board.ROWS), pygame.SRCALPHA)

        self.playerSquares = [(0, Board.ROWS - 1)]
        self.opponentSquares = [(Board.COLUMNS - 1, 0)]

    def create_board(self) -> list:
        new_board = []

        for _c in range(Board.COLUMNS):
            old_square = -1
            new_column = []
            for _r in range(Board.ROWS):
                options = set(range(6))
                options.discard(old_square)
                if len(new_board) > 0: options.discard(new_board[-1][len(new_column)])
                if len(new_board) + 1 == Board.COLUMNS and len(new_column) == 0: options.discard(new_board[0][-1])
                new_square = random.choice(list(options))
                new_column.append(new_square)
                old_square = new_square
            new_board.append(new_column)

        return new_board

    def update(self):
        self.animation += 1

    def refresh(self):
        if self.game.turn:
            self.game.simulator.simulate(self.board, self.game.turn)
            self.game.simulator.collapse()
            print(self.game.simulator.bestChoice)

        self.animation = 0
        for column in range(Board.COLUMNS):
            for row in range(Board.ROWS):
                pygame.draw.rect(self.tempSurface, color.COLORS[self.board[column][row]] + (100,),
                                (column*Board.SQUARE_SIZE, row*Board.SQUARE_SIZE, Board.SQUARE_SIZE, Board.SQUARE_SIZE))

    def draw(self):
        if self.animation % 100 == 70:
            for square in [self.playerSquares, self.opponentSquares][self.game.turn]:
                column, row = square
                if self.board[column][row] == [self.game.player, self.game.opponent][self.game.turn]:
                        pygame.draw.rect(self.tempSurface, color.COLORS[[self.game.player, self.game.opponent][self.game.turn]] + (15,),
                                        (column*Board.SQUARE_SIZE, row*Board.SQUARE_SIZE, Board.SQUARE_SIZE, Board.SQUARE_SIZE))
        elif self.animation % 100 == 20:
            if self.game.playerScore + self.game.opponentScore == Board.COLUMNS * Board.ROWS:
                self.game.gameover = True
            for square in [self.playerSquares, self.opponentSquares][self.game.turn]:
                column, row = square
                if self.board[column][row] == [self.game.player, self.game.opponent][self.game.turn]:
                        pygame.draw.rect(self.tempSurface, (255, 255, 255, 5),
                                        (column*Board.SQUARE_SIZE, row*Board.SQUARE_SIZE, Board.SQUARE_SIZE, Board.SQUARE_SIZE))

        self.surface.blit(self.tempSurface, (0, 0))
        
        self.game.surface.blit(self.surface, (self.game.WIDTH/2 - Board.SQUARE_SIZE*Board.COLUMNS/2, self.game.HEIGHT/2 - Board.SQUARE_SIZE*Board.ROWS/2))
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

            if column < Board.COLUMNS - 1 and check(column + 1, row):
                squares.append((column + 1, row))
            if column > 0 and check(column - 1, row):
                squares.append((column - 1, row))
            if row < Board.ROWS - 1 and check(column, row + 1):
                squares.append((column, row + 1))
            if row > 0 and check(column, row - 1):
                squares.append((column, row - 1))


