
import pygame
import math
import random
import color, id
from Board import Board
from Panel import Panel
from Simulator import Simulator

class Game:
    def __init__(self, surface, mode):
        self.WIDTH = surface.get_width()
        self.HEIGHT = surface.get_height()
        self.surface = surface
        self.tick = 0
        self.gameover = False
        self.mode = mode

        self.board = Board(self)
        self.panel = Panel(self)

        # 0: player, 1: opponent
        self.turn = 0
        self.timer = 0

        self.simulator = Simulator()

        self.refresh()

    def start(self):
        pass

    def update(self):
        self.board.update()

        if self.mode == id.PERSON or not self.turn:
            self.timer += 1

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


