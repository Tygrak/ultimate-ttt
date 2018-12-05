import random
import math
import datetime
from Board import Board

def GreedySearchGetMove(board):
    moves = board.getMoves()
    bestMove = None
    for move in moves:
        state = board.clone()
        state.makeMove(move[0], move[1])
        if state.wonBy == board.getCurrentPlayer():
            return move
        if state.boards[move[0]].wonBy == board.getCurrentPlayer():
            bestMove = move
    if bestMove == None:
        return board.getRandomMove()
    else:
        return bestMove