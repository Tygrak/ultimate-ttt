import random
import math
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

    def startGame(self, verbose = True):
        self.resetValues()
        board = Board()
        if verbose: board.printBoard()
        while board.wonBy == 0:
            def makePlayerMove():
                nextMove = True
                while nextMove:
                    try:
                        nextMove = input().strip().split(" ")
                        if verbose: print(str(board.getMoves()) + " -> " + str(nextMove))
                        board.makeMove(int(nextMove[0]), int(nextMove[1]))
                        if verbose: board.printBoard()
                        if verbose: print(str(board.getMoves()))
                        break
                    except:
                        pass
            def makeAIMove():
                nextMove = MonteCarloGetMove(board, self.player1Iterations if board.getCurrentPlayer() == 1 else self.player2Iterations, verbose)
                if verbose: print(str(board.getMoves()) + " -> " + str(nextMove))
                board.makeMove(int(nextMove[0]), int(nextMove[1]))
                if verbose: board.printBoard()
                if verbose: print(str(board.getMoves()))
                sleep(self.sleepAfterAITurn)

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
