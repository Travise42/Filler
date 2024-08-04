import pygame
import math
import id, color
from Board import Board

class Panel:

    def __init__(self, game = None, engine = None):
        self.game = game
        self.engine = engine
        self.gameAndEngine = game if game != None else engine
        self.surface = pygame.Surface((Board.SQUARE_SIZE*6, Board.SQUARE_SIZE), pygame.SRCALPHA)

        self.windowX = self.gameAndEngine.WIDTH/2 - Board.SQUARE_SIZE*3
        self.windowY = self.gameAndEngine.HEIGHT - Board.SQUARE_SIZE*2

    def update(self):
        pass

    def refresh(self):
        self.surface.fill((0, 0, 0, 0))

        for i in range(6):
            if ( self.engine != None and self.engine.selectedColor == i ) or (
                 self.game != None and ( i == self.game.player or i == self.game.opponent )):
                rect = ((i+0.3)*Board.SQUARE_SIZE, 0.3*Board.SQUARE_SIZE, 0.4*Board.SQUARE_SIZE, 0.4*Board.SQUARE_SIZE)
            else:
                rect = (i*Board.SQUARE_SIZE, 0, Board.SQUARE_SIZE, Board.SQUARE_SIZE)
            pygame.draw.rect(self.surface, color.COLORS[i], rect)

    def draw(self):
        if self.game != None and self.game.mode and self.game.turn:
            return
        
        self.gameAndEngine.surface.blit(self.surface, (self.windowX, self.windowY))

    def click(self):
        if self.game != None and self.game.mode and self.game.turn:
            return
        
        mouseX = int((pygame.mouse.get_pos()[0] - self.windowX) / Board.SQUARE_SIZE)
        mouseY = pygame.mouse.get_pos()[1] - self.windowY

        if mouseX < 0 or mouseX >= 6:
            return
        if mouseY < 0 or mouseY >= Board.SQUARE_SIZE:
            return
        
        if self.game != None:
            if mouseX == self.game.player or mouseX == self.game.opponent:
                return
            self.game.board.makeMove(mouseX)
            return
        
        if mouseX == self.engine.selectedColor:
            return
        self.engine.selectedColor = mouseX
        