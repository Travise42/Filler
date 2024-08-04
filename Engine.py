import pygame
import id, color
from Panel import Panel
from Board import Board

class Engine:

    def __init__(self, surface):
        self.WIDTH = surface.get_width()
        self.HEIGHT = surface.get_height()
        self.surface = surface
        self.boardSurface = pygame.Surface((Board.SQUARE_SIZE*Board.COLUMNS, Board.SQUARE_SIZE*Board.ROWS))

        self.board = [[id.BLACK for _r in range(Board.ROWS)] for _c in range(Board.COLUMNS)]

        self.boardX = self.WIDTH/2 - self.boardSurface.get_width()/2
        self.boardY = self.HEIGHT/2 - self.boardSurface.get_height()/2

        self.panel = Panel(engine=self)

        self.selectedColor = id.BLACK

        self.refresh()

    def click(self):
        mouseColumn = int( ( pygame.mouse.get_pos()[0] - self.boardX ) / Board.SQUARE_SIZE )
        mouseRow = int( ( pygame.mouse.get_pos()[1] - self.boardY ) / Board.SQUARE_SIZE )

        if mouseColumn not in range(Board.COLUMNS) or mouseRow not in range(Board.ROWS):
            self.panel.click()
        else:
            self.swapColor(mouseColumn, mouseRow, self.selectedColor)

        self.refresh()

    def swapColor(self, column, row, color):
        self.board[column][row] = color

    def refresh(self):
        for column, squares in enumerate(self.board):
            for row, square in enumerate(squares):
                pygame.draw.rect(self.boardSurface, color.COLORS[square],
                                 (Board.SQUARE_SIZE*column, Board.SQUARE_SIZE*row,
                                  Board.SQUARE_SIZE, Board.SQUARE_SIZE))
                
        self.panel.refresh()

    def draw(self):
        self.surface.blit(self.boardSurface, (self.boardX, self.boardY))
        self.panel.draw()
