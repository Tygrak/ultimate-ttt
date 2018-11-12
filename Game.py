import random
import math
import sys
from Board import Board 
from time import sleep
from MCTreeSearch import MonteCarloGetMove

class Game:
    def __init__(self):
        self.player1IsAI = False
        self.player2IsAI = True
        self.player1Iterations = 100
        self.player2Iterations = 100
        self.gameTurn = 0
        self.gameResult = 0
        self.sleepAfterAITurn = 0.5
        self.useTimer = False

    def startGame(self, verbose = True):
        def makePlayerMove():
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
                if verbose: print(str(board.getMoves()) + " -> " + str(nextMove))
                board.makeMove(int(nextMove[0]), int(nextMove[1]))
                nextMove = False
                if verbose: board.printBoard()
                if verbose: print(str(board.getMoves()))
        def makeAIMove():
            nextMove = MonteCarloGetMove(board, self.player1Iterations if board.getCurrentPlayer() == 1 else self.player2Iterations, verbose, useTimer=self.useTimer)
            if verbose: print(str(board.getMoves()) + " -> " + str(nextMove))
            board.makeMove(int(nextMove[0]), int(nextMove[1]))
            if verbose: board.printBoard()
            if verbose: print(str(board.getMoves()))
            sleep(self.sleepAfterAITurn)

        self.resetValues()
        board = Board()
        if verbose: board.printBoard()
        while board.wonBy == 0:
            self.gameTurn += 1
            if board.getCurrentPlayer() == 1:
                if self.player1IsAI:
                    makeAIMove()
                else:
                    makePlayerMove()
            else:
                if self.player2IsAI:
                    makeAIMove()
                else:
                    makePlayerMove()
        if verbose: print("Game was won by player " + str(board.wonBy))
        self.gameResult = board.wonBy

    def resetValues(self):
        self.gameResult = 0
        self.gameTurn = 0
