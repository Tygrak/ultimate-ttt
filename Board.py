import random
from SmallBoard import SmallBoard 

class Board:
    def __init__(self, lastPlayer = 2):
        self.boards = [SmallBoard() for i in range(3*3)] #1D arrays are faster than 2D arrays
        self.lastPlayer = lastPlayer
        self.lastMove = None
        self.wonBy = 0
    
    def clone(self):
        newBoard = Board(self.lastPlayer)
        newBoard.lastMove = self.lastMove
        for i in range(9):
            newBoard.boards[i] = self.boards[i].clone()
        return newBoard

    def get1D(self, board, pos):
        return self.boards[board].get(pos)

    def get2D(self, board, x, y):
        return self.boards[board].get(x+y*3)

    def change(self, board, pos, value):
        self.boards[board].change(pos, value)

    def getCurrentPlayer(self):
        return 1 if self.lastPlayer == 2 else 2

    def makeMove(self, board, pos):
        self.change(board, pos, self.getCurrentPlayer())
        self.lastMove = pos
        self.lastPlayer = self.getCurrentPlayer()
        self.boards[board].checkWin()
        self.checkWin()

    def makeMoveNoWinCheck(self, board, pos):
        self.change(board, pos, self.getCurrentPlayer())
        self.lastMove = pos
        self.lastPlayer = self.getCurrentPlayer()
        self.boards[board].checkWin()

    def getMoves(self):
        if self.lastMove != None:
            board = self.boards[self.lastMove]
            if board.wonBy == 0:
                boardMoves = board.getMoves()
                return [(self.lastMove, boardMoves[i]) for i in range(len(boardMoves))]
        moves = []
        for i in range(9):
            if self.boards[i].wonBy == 0:
                boardMoves = self.boards[i].getMoves()
                moves.extend([(i, boardMoves[j]) for j in range(len(boardMoves))])
        return moves

    def getRandomMove(self):
        if self.lastMove != None:
            board = self.boards[self.lastMove]
            if board.wonBy == 0:
                boardMoves = board.getMoves()
                return (self.lastMove, random.choice(boardMoves))
        moves = []
        for i in range(9):
            if self.boards[i].wonBy == 0:
                boardMoves = self.boards[i].getMoves()
                moves.extend([(i, boardMoves[j]) for j in range(len(boardMoves))])
        return random.choice(moves)
    
    def checkWin(self):
        for i in range(3):
            if self.boards[i*3].wonBy == self.boards[1+i*3].wonBy and self.boards[i*3].wonBy == self.boards[2+i*3].wonBy and self.boards[i*3].wonBy != 0:
                self.wonBy = self.boards[i*3].wonBy
        for i in range(3):
            if self.boards[i].wonBy == self.boards[i+3].wonBy and self.boards[i].wonBy == self.boards[i+6].wonBy and self.boards[i].wonBy != 0:
                self.wonBy = self.boards[i].wonBy
        if self.boards[0].wonBy == self.boards[4].wonBy and self.boards[0].wonBy == self.boards[8].wonBy and self.boards[0].wonBy != 0:
            self.wonBy = self.boards[0].wonBy
        if self.boards[2].wonBy == self.boards[4].wonBy and self.boards[2].wonBy == self.boards[6].wonBy and self.boards[2].wonBy != 0:
            self.wonBy = self.boards[2].wonBy
        if self.wonBy == 0 and len(self.getMoves()) == 0:
            self.wonBy = 3

    def boardToArray(self):
        board = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    board.append(self.get2D(k+i*3, 0, j))
                    board.append(self.get2D(k+i*3, 1, j))
                    board.append(self.get2D(k+i*3, 2, j))
        return board

    def printBoard(self):
        board = self.boardToArray()
        for y in range(9):
            toPrint = ""
            for x in range(9):
                square = board[x+y*9]
                if square == 1:
                    toPrint += "X"
                elif square == 2:
                    toPrint += "O"
                else:
                    toPrint += "."
                if x == 2 or x == 5:
                    toPrint += "|"
                else:
                    toPrint += " "
            print(toPrint)
            if y == 2 or y == 5:
                print("-----------------")