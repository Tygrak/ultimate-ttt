import random
import math
import sys

from Board import Board 
from time import sleep
from MCTreeSearch import MonteCarloGetMove
from GreedySearch import GreedySearchGetMove

class Game:
    def __init__(self):
        self.player1IsAI = False
        self.player2IsAI = True
        self.player1Iterations = 100
        self.player2Iterations = 100
        self.player1UseGreedyAI = False
        self.player2UseGreedyAI = False
        self.gameTurn = 0
        self.gameResult = 0
        self.sleepAfterAITurn = 0.5
        self.useTimer = False
        self.board = None
        self.verbose = True
        self.allowCheating = False

    def makePlayerMove(self):
        nextMove = True
        while nextMove:
            nextMove = input().strip().split(" ")
            if nextMove[0] == "quit" or nextMove[0] == "exit":
                sys.exit()
            # Input check
            if not len(nextMove) == 2:
                print("Invalid input, correct input in format 'n n', where n is from 0 to 9")
                continue
            if not nextMove[0].isnumeric() or not nextMove[1].isnumeric():
                print("Invalid input, correct input in format 'n n', where n is from 0 to 9")
                continue
            if int(nextMove[0]) < 0 or int(nextMove[0]) > 8 or int(nextMove[1]) < 0 or int(nextMove[1]) > 8:
                print("Invalid input, correct input in format 'n n', where n is from 0 to 9")
                continue
            if (int(nextMove[0]), int(nextMove[1])) not in self.board.getMoves() and not self.allowCheating:
                print("Invalid move, your available moves are: " + str(self.board.getMoves()))
                continue
            if self.verbose: print(str(self.board.getMoves()) + " -> " + str(nextMove))
            self.board.makeMove(int(nextMove[0]), int(nextMove[1]))
            nextMove = False
            if self.verbose: self.board.printBoard()
            if self.verbose: print(str(self.board.getMoves()))

    def makeAIMove(self):
        nextMove = None
        if (self.board.getCurrentPlayer() == 1 and self.player1UseGreedyAI) or (self.board.getCurrentPlayer() == 2 and self.player2UseGreedyAI):
            nextMove = GreedySearchGetMove(self.board)
        else:
            nextMove = MonteCarloGetMove(self.board, 
                self.player1Iterations if self.board.getCurrentPlayer() == 1 else self.player2Iterations,
                self.verbose,
                useTimer=self.useTimer)
        if self.verbose: print(str(self.board.getMoves()) + " -> " + str(nextMove))
        self.board.makeMove(int(nextMove[0]), int(nextMove[1]))
        if self.verbose: self.board.printBoard()
        if self.verbose: print("Available moves: " + str(self.board.getMoves()))
        sleep(self.sleepAfterAITurn)

    def startGame(self):
        self.resetValues()
        self.board = Board()
        if self.verbose: self.board.printBoard()
        while self.board.wonBy == 0:
            self.gameTurn += 1
            if self.board.getCurrentPlayer() == 1:
                if self.player1IsAI:
                    self.makeAIMove()
                else:
                    self.makePlayerMove()
            else:
                if self.player2IsAI:
                    self.makeAIMove()
                else:
                    self.makePlayerMove()
        if self.verbose: print("Game was won by player " + str(self.board.wonBy))
        self.gameResult = self.board.wonBy

    def resetValues(self):
        self.gameResult = 0
        self.gameTurn = 0
