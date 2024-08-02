import math
from Board import Board
from Simulation import Simulation

class Simulator:

    def __init__(self):
        self.running = False


    def simulate(self, board, turn, depth):
        self.running = True

        playerSquares = self.get_squares(board, 0, Board.ROWS - 1)
        opponentSquares = self.get_squares(board, Board.COLUMNS - 1, 0)

        self.simulation = Simulation(board, -1, turn, playerSquares, opponentSquares, depth)

        self.simulation.collapse()
        self.bestChoice = self.simulation.bestChoice

        self.running = False


    def get_squares(self, board, initial_column, initial_row):
        squares = [(initial_column, initial_row)]
        square_color = board[initial_column][initial_row]
        for column in range(Board.COLUMNS):
            for row in range(Board.ROWS):
                if (column, row) in squares or board[column][row] != square_color:
                    continue

                t = 0
                if column < Board.COLUMNS - 1 and square_color == board[column + 1][row]:
                    t = 1
                    if (column + 1, row) not in squares:
                        squares.append((column + 1, row))
                if column > 0 and square_color == board[column - 1][row]:
                    t = 1
                    if (column - 1, row) not in squares:
                        squares.append((column - 1, row))
                if row < Board.ROWS - 1 and square_color == board[column][row + 1]:
                    t = 1
                    if (column, row + 1) not in squares:
                        squares.append((column, row + 1))
                if row > 0 and square_color == board[column][row - 1]:
                    t = 1
                    if (column, row - 1) not in squares:
                        squares.append((column, row - 1))
                if t == 1:
                    squares.append((column, row))
        
        return squares



