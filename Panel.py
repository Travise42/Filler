import pygame
import id, color
from Board import Board

class Panel:

    def __init__(self):
        self.surface = pygame.Surface((Board.SQUARE_SIZE*6, Board.SQUARE_SIZE))

        self.refresh()

    def update(self):
        pass

    def refresh(self):
        for i in range(6):
            pygame.draw.rect(self.surface, color.COLORS[i],
                             (i*Board.SQUARE_SIZE, 0, Board.SQUARE_SIZE, Board.SQUARE_SIZE))

    def draw(self, surf, width, height):
        surf.blit(self.surface, (width/2 - Board.SQUARE_SIZE*3, height - Board.SQUARE_SIZE*2))