import pygame
import math
import id, color
from Board import Board

class Panel:

    def __init__(self, game):
        self.game = game
        self.surface = pygame.Surface((Board.SQUARE_SIZE*6, Board.SQUARE_SIZE), pygame.SRCALPHA)

        self.windowX = self.game.WIDTH/2 - Board.SQUARE_SIZE*3
        self.windowY = self.game.HEIGHT - Board.SQUARE_SIZE*2

    def update(self):
        pass

    def refresh(self):
        self.surface.fill((0, 0, 0, 0))

        for i in range(6):
            if i == self.game.player or i == self.game.opponent:
                rect = ((i+0.3)*Board.SQUARE_SIZE, 0.3*Board.SQUARE_SIZE, 0.4*Board.SQUARE_SIZE, 0.4*Board.SQUARE_SIZE)
            else:
                rect = (i*Board.SQUARE_SIZE, 0, Board.SQUARE_SIZE, Board.SQUARE_SIZE)
            pygame.draw.rect(self.surface, color.COLORS[i], rect)

    def draw(self):
        self.game.surface.blit(self.surface, (self.windowX, self.windowY))

    def click(self, pos):
        mouseX = int((pos[0] - self.windowX) / Board.SQUARE_SIZE)
        mouseY = pos[1] - self.windowY

        if mouseX < 0 or mouseX >= 6:
            return
        if mouseY < 0 or mouseY >= Board.SQUARE_SIZE:
            return
        if mouseX == self.game.player or mouseX == self.game.opponent:
            return
        
        self.game.board.changePlayerColor(mouseX)
        
        self.game.refresh()
        