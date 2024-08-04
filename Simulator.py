import math
from Board import Board
from Simulation import Simulation

class Simulator:

    def __init__(self):
        self.running = False


    def simulate(self, board, turn, depth):
        self.running = True

        playerSquares = Board.get_squares(board, 0, Board.ROWS - 1)
        opponentSquares = Board.get_squares(board, Board.COLUMNS - 1, 0)

        self.simulation = Simulation(board, -1, turn, playerSquares, opponentSquares, depth)

        self.simulation.collapse()
        self.bestChoice = self.simulation.bestChoice

        self.running = False




