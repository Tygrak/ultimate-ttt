from Game import Game
import time

for i in range(100):
    startTime = time.time()
    game = Game()
    game.sleepAfterAITurn = 0.0
    game.player1IsAI = True
    game.player2IsAI = True
    game.player1Iterations = 100
    game.player2Iterations = 100
    game.startGame(False)
    timeToFinish = time.time() - startTime
    print("Game " + str(i) + " finished in " + str(timeToFinish) + ": " + str(game.player1Iterations) + ", " + str(game.player2Iterations) + ", " + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")
    with open("results.txt", "a") as outputFile:
        outputFile.write(str(game.player1Iterations) + ", " + str(game.player2Iterations) + ", " + str(game.gameResult) + ", " + str(game.gameTurn) + "\n")
