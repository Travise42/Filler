
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
        self.panel = Panel(self)

        # 0: player, 1: opponent
        self.turn = 0

        self.refresh()

    def start(self):
        pass

    def update(self):
        pass

    def refresh(self):
        self.player = self.board.getPlayer()
        self.opponent = self.board.getOpponent()

        self.board.refresh()
        self.panel.refresh()

    def draw(self):
        self.board.draw(self.surface, self.WIDTH, self.HEIGHT)
        self.panel.draw(self.surface)
        self.tick += 1


