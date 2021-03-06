import random
import math
import datetime
from Board import Board

class Node:
    def __init__(self, board, move = None, parent = None):
        self.move = move # last move, None for root
        self.parentNode = parent # None for the root node
        self.childNodes = []
        self.visits = 0
        self.wins = 0
        self.untriedMoves = board.getMoves()
        self.lastPlayer = board.lastPlayer
   
    def selectChild(self):
        #Select child using the UCT formula
        def getUCTValue(node):
            return node.wins/node.visits + 1.414*math.sqrt(math.log(self.visits)/node.visits)
        bestValue = getUCTValue(self.childNodes[0])
        bestIndex = 0
        for i in range(1, len(self.childNodes)):
            value = getUCTValue(self.childNodes[i])
            #print(value, self.childNodes[i].visits, self.childNodes[i].wins)
            if value > bestValue:
                #print(value, self.childNodes[i].visits, self.childNodes[i].wins)
                bestValue = value
                bestIndex = i
        return self.childNodes[bestIndex]

    def addChild(self, board, move):
        newNode = Node(board, move, self)
        self.untriedMoves.remove(move)
        self.childNodes.append(newNode)
        return newNode

    def update(self, result):
        self.visits += 1
        self.wins += result

#Monte Carlo tree search
#If use timer is true, instead use max thinking time as seconds
def MonteCarloGetMove(board, maxIterations, verbose = True, useTimer = False):
    rootNode = Node(board)
    timer = maxIterations
    startTime = datetime.datetime.now()
    if useTimer:
        maxIterations = 1000000
    for i in range(maxIterations):
        node = rootNode
        state = board.clone()
        if useTimer:
            if (datetime.datetime.now() - startTime).total_seconds() > timer:
                break
        #Select
        while node.untriedMoves == [] and node.childNodes != []:
            node = node.selectChild()
            state.makeMoveNoWinCheck(node.move[0], node.move[1])
        state.checkWin()

        #Expand
        if len(node.untriedMoves) != 0:    
            move = random.choice(node.untriedMoves) 
            state.makeMove(move[0], move[1])
            node = node.addChild(state, move)

        #Rollout
        while state.wonBy == 0:
            move = state.getRandomMove()
            state.makeMove(move[0], move[1])
                
        #Backpropagate
        while node != None:
            if state.wonBy == 3:
                node.update(0.0625)
            elif state.wonBy == node.lastPlayer:
                node.update(1)
            else:
                node.update(0)
            node = node.parentNode
    bestIndex = 0
    bestVisits = rootNode.childNodes[0].visits
    for i in range(1, len(rootNode.childNodes)):
        if rootNode.childNodes[i].visits > bestVisits:
            bestVisits = rootNode.childNodes[i].visits
            bestIndex = i
    if verbose: print("From " + str(len(rootNode.childNodes)) + " best node had " + str(bestVisits) + " visits and " + str(rootNode.childNodes[bestIndex].wins) + " wins.")
    return rootNode.childNodes[bestIndex].move
