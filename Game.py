
import pygame
import math
import random
import color, id
from Board import Board
from Panel import Panel

class Game:
    def __init__(self, surface, size):
        self.WIDTH = size[0]
        self.HEIGHT = size[1]
        self.surface = surface
        self.tick = 0

        self.board = Board()
        self.panel = Panel()

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.board.draw(self.surface, self.WIDTH, self.HEIGHT)
        self.panel.draw(self.surface, self.WIDTH, self.HEIGHT)
        self.tick += 1


