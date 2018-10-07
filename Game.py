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
        self.sleepAfterAITurn = 0.5

    def startGame(self):
        board = Board()
        board.printBoard()
        while board.wonBy == 0:
            def makePlayerMove():
                nextMove = input().strip().split(" ")
                print(str(board.getMoves()) + " -> " + str(nextMove))
                board.makeMove(int(nextMove[0]), int(nextMove[1]))
                board.printBoard()
                print(str(board.getMoves()))
            def makeAIMove():
                nextMove = MonteCarloGetMove(board, self.player1Iterations if board.getCurrentPlayer() == 1 else self.player2Iterations)
                print(str(board.getMoves()) + " -> " + str(nextMove))
                board.makeMove(int(nextMove[0]), int(nextMove[1]))
                board.printBoard()
                print(str(board.getMoves()))
                sleep(self.sleepAfterAITurn)
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
        print("Game was won by player " + str(board.wonBy))
