
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
        self.gameover = False

        self.board = Board(self)
        self.panel = Panel(self)

        # 0: player, 1: opponent
        self.turn = 0

        self.refresh()

    def start(self):
        pass

    def update(self):
        self.board.update()

    def refresh(self):
        self.player = self.board.getPlayer()
        self.opponent = self.board.getOpponent()
        self.playerScore = len(self.board.playerSquares)
        self.opponentScore = len(self.board.opponentSquares)

        self.board.refresh()
        self.panel.refresh()

    def draw(self):
        self.board.draw()
        self.panel.draw()
        self.tick += 1


