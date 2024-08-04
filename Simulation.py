# Simulation Classes are run by the Simulator Class
# These Simulation Classes take in a Simulation which contains its game's state
# Then creates 6 Simulations off of that first Simualtions
# These new Simulations can be put into more Simulations using the Simulator Class

import math, time, random
from Board import Board

class Simulation:
    def __init__(self, board, new_color, turn, playerSquares, opponentSquares, remainingGenerations):
        self.board = board
        self.turn = turn
        self.remainingGenerations = remainingGenerations
        self.color = new_color
        
        self.playerSquares = list(playerSquares)
        self.opponentSquares = list(opponentSquares)

        if remainingGenerations > 0:
            self.simulations = [self.simulate(new_color) for new_color in range(6)]

    def simulate(self, new_color):
        board = [list(row) for row in self.board]

        # Not a valid color to pick
        if new_color == board[0][Board.ROWS - 1] or new_color == board[Board.COLUMNS - 1][0]:
            return Simulation([], new_color, 0, [], [], 0)

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

        #if len([self.playerSquares, self.opponentSquares][self.turn]) == len(squares):
        #    return Simulation([], new_color, 0, [], [], 0)

        # Create a new simulation with this game state
        gameOver = len([self.playerSquares, self.opponentSquares][not self.turn]) + len(squares) == Board.COLUMNS * Board.ROWS
        return Simulation(board, new_color, 1 - self.turn,
                          [squares, self.playerSquares][self.turn],
                          [self.opponentSquares, squares][self.turn],
                          0 if gameOver else self.remainingGenerations - 1)
    
    def collapse(self):
        if self.remainingGenerations == 0:
            self.bestChoice = self.color
            return

        for simulation in self.simulations:
            simulation.collapse()
    
        self.simulations = [max(self.simulations, key=self.value)]
    
        self.playerSquares = self.simulations[0].playerSquares
        self.opponentSquares = self.simulations[0].opponentSquares

        self.bestChoice = self.simulations[0].color

    def value(self, simulation):
        primary, secondary = len(simulation.playerSquares), len(simulation.opponentSquares)
        if self.turn:
            primary, secondary = secondary, primary
        
        return 5*primary - secondary



                

