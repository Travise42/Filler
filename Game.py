
import pygame
import math
import random
import color, id
from Board import Board
from Panel import Panel
from Simulator import Simulator
import threading

class Game:
    def __init__(self, surface, mode, engine=None):
        self.WIDTH = surface.get_width()
        self.HEIGHT = surface.get_height()
        self.surface = surface
        self.tick = 0
        self.gameover = False
        self.mode = mode
        self.engine = engine != None

        self.board = Board(self, engine)
        self.panel = Panel(game=self)

        # 0: player, 1: opponent
        self.turn = 1
        self.timer = 10

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

        if self.engine:
            threading.Thread(target=self.simulator.simulate(self.board.board, self.turn, 10)).start()

        self.board.refresh()
        self.panel.refresh()

    def draw(self):
        self.board.draw()
        self.panel.draw()
        self.tick += 1

        if self.engine and not self.simulator.running:
            pygame.draw.rect(self.surface, color.COLORS[self.simulator.bestChoice],
                             (self.WIDTH - Board.SQUARE_SIZE*2, self.HEIGHT - Board.SQUARE_SIZE*2, Board.SQUARE_SIZE, Board.SQUARE_SIZE))


