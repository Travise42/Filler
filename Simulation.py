# Simulation Classes are run by the Simulator Class
# These Simulation Classes take in a Simulation which contains its game's state
# Then creates 6 Simulations off of that first Simualtions
# These new Simulations can be put into more Simulations using the Simulator Class

import math
from Board import Board

class Simulation:
    def __init__(self, board, turn, playerSquares, opponentSquares, remainingGenerations):
        self.board = board
        self.turn = turn
        self.remainingGenerations = remainingGenerations
        
        self.playerSquares = list(playerSquares)
        self.opponentSquares = list(opponentSquares)

        if remainingGenerations > 0:
            self.simulations = [self.simulate(new_color) for new_color in range(6)]

    def simulate(self, new_color):
        board = [list(row) for row in self.board]

        # Not a valid color to pick
        if new_color == board[0][Board.ROWS - 1] or new_color == board[Board.COLUMNS - 1][0]:
            return Simulation([], 0, [], [], self.remainingGenerations - 1)

        squares = list([self.playerSquares, self.opponentSquares][self.turn])

        def check(column, row):
            return board[column][row] == new_color and (column, row) not in squares

        for square in squares:
            column, row = square

            board[column][row] = new_color

            if column < Board.COLUMNS - 1 and check(column + 1, row):
                squares.append((column + 1, row))
            if column > 0 and check(column - 1, row):
                squares.append((column - 1, row))
            if row < Board.ROWS - 1 and check(column, row + 1):
                squares.append((column, row + 1))
            if row > 0 and check(column, row - 1):
                squares.append((column, row - 1))

        # Create a new simulation with this game state
        return Simulation(board, 1 - self.turn,
                          [squares, self.playerSquares][self.turn],
                          [self.opponentSquares, squares][self.turn],
                          self.remainingGenerations - 1)
                

