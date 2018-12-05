from Game import Game
import time

def PlayGeneric(player1IsAI, player2IsAI, player1UseGreedyAI, player2UseGreedyAI,
                 player1Iterations, player2Iterations, useTimer = False, sleepAfterAITurn = 0.0):
    game = Game()
    game.sleepAfterAITurn = 0.0
    game.useTimer = useTimer
    game.player1IsAI = player1IsAI
    game.player2IsAI = player2IsAI
    game.player1UseGreedyAI = player1UseGreedyAI
    game.player2UseGreedyAI = player2UseGreedyAI
    game.player1Iterations = player1Iterations
    game.player2Iterations = player2Iterations
    startTime = time.time()
    game.startGame()
    timeToFinish = time.time() - startTime
    print("Game finished in " + str(timeToFinish) + ": " + str(game.player1Iterations) + ", "
     + str(game.player2Iterations) + ", " + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")
    with open("results.txt", "a") as outputFile:
        outputFile.write(str(game.player1Iterations) + ", " + str(game.player2Iterations) + ", "
         + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")

def PlayAgainstAI(AIIterations, playAsPlayer1 = True, useTimer = False):
    if playAsPlayer1:
        PlayGeneric(False, True, False, False, -1, AIIterations, useTimer)
    else:
        PlayGeneric(True, False, False, False, AIIterations, -1, useTimer)

def PlayAgainstGreedyAI(playAsPlayer1 = True):
    if playAsPlayer1:
        PlayGeneric(False, True, False, True, -1, -4, False)
    else:
        PlayGeneric(True, False, True, False, -4, -1, False)

def RunAI(player1Iterations, start, step, stop, gamesPer):
    game = Game()
    game.sleepAfterAITurn = 0.0
    if player1Iterations == -4:
        game.player1UseGreedyAI = True
    game.player1IsAI = True
    game.player2IsAI = True
    game.verbose = False
    for j in range(start, stop+step, step):
        game.player1Iterations = player1Iterations
        game.player2Iterations = j
        setTime = time.time()
        for i in range(gamesPer):
            startTime = time.time()
            game.startGame()
            timeToFinish = time.time() - startTime
            print("Game " + str(i) + " finished in " + str(timeToFinish) + ": " + str(game.player1Iterations)
             + ", " + str(game.player2Iterations) + ", " + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")
            with open("results.txt", "a") as outputFile:
                outputFile.write(str(game.player1Iterations) + ", " + str(game.player2Iterations)
                 + ", " + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")
        setTimeToFinish = time.time() - setTime
        print("Game set " + str(game.player1Iterations) + ":" + str(game.player2Iterations) + " finished running in " + str(setTimeToFinish))
