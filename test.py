from Game import Game
import time

def PlayAgainstAI(AIIterations, playAsPlayer1 = True, useTimer = False):
    game = Game()
    game.sleepAfterAITurn = 0.0
    game.useTimer = useTimer
    if playAsPlayer1:
        game.player1IsAI = False
        game.player2IsAI = True
        game.player1Iterations = -1
        game.player2Iterations = AIIterations
    else:
        game.player1IsAI = True
        game.player2IsAI = False
        game.player1Iterations = AIIterations
        game.player2Iterations = -1
    startTime = time.time()
    game.startGame(True)
    timeToFinish = time.time() - startTime
    print("Game finished in " + str(timeToFinish) + ": " + str(game.player1Iterations) + ", " + str(game.player2Iterations) + ", " + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")
    with open("results.txt", "a") as outputFile:
        outputFile.write(str(game.player1Iterations) + ", " + str(game.player2Iterations) + ", " + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")

def RunAI(player1Iterations, start, step, stop, gamesPer):
    game = Game()
    game.sleepAfterAITurn = 0.0
    game.player1IsAI = True
    game.player2IsAI = True
    for j in range(start, stop+step, step):
        game.player1Iterations = player1Iterations
        game.player2Iterations = j
        setTime = time.time()
        for i in range(gamesPer):
            startTime = time.time()
            game.startGame(False)
            timeToFinish = time.time() - startTime
            print("Game " + str(i) + " finished in " + str(timeToFinish) + ": " + str(game.player1Iterations) + ", " + str(game.player2Iterations) + ", " + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")
            with open("results.txt", "a") as outputFile:
                outputFile.write(str(game.player1Iterations) + ", " + str(game.player2Iterations) + ", " + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")
        setTimeToFinish = time.time() - setTime
        print("Game set " + str(game.player1Iterations) + ":" + str(game.player2Iterations) + " finished running in " + str(setTimeToFinish))

#RunAI(150, 525, 25, 550, 50)
#PlayAgainstAI(7500, False)
PlayAgainstAI(10, False, True)