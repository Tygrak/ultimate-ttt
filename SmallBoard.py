class SmallBoard:
    def __init__(self):
        self.board = [0 for i in range(3*3)]
        self.wonBy = 0
    
    def clone(self):
        newBoard = SmallBoard()
        newBoard.wonBy = self.wonBy
        newBoard.board = self.board.copy()
        return newBoard

    def get(self, pos):
        return self.board[pos]
    
    def change(self, pos, value):
        self.board[pos] = value
    
    def isOcuppied(self, pos):
        if self.get(pos) == 0:
            return False
        else:
            return True
    
    def checkWin(self):
        for i in range(3):
            if self.get(i*3) == self.get(1+i*3) and self.get(i*3) == self.get(2+i*3) and self.get(i*3) != 0:
                self.wonBy = self.get(i*3)
        for i in range(3):
            if self.get(i) == self.get(i+3) and self.get(i) == self.get(i+6) and self.get(i) != 0:
                self.wonBy = self.get(i) 
        if self.get(0) == self.get(4) and self.get(0) == self.get(8) and self.get(0) != 0:
            self.wonBy = self.get(0) 
        if self.get(2) == self.get(4) and self.get(2) == self.get(6) and self.get(2) != 0:
            self.wonBy = self.get(2) 
        if self.wonBy == 0 and len(self.getMoves()) == 0:
            self.wonBy = 3

    def getMoves(self):
        if self.wonBy != 0:
            return []
        moves = []
        for i in range(9):
            if not self.isOcuppied(i):
                moves.append(i)
        return moves