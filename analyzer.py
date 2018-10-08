import matplotlib.pyplot as plt

class Result:
    def __init__(self, player1Iters, player2Iters, gameResult, gameTurns):
        self.player1Iters = player1Iters
        self.player2Iters = player2Iters
        self.gameResult = gameResult
        self.gameTurns = gameTurns

def getResultsWhere(results, player1Iters, player2Iters):
    newResults = []
    for result in results:
        if result.player1Iters == player1Iters and result.player2Iters == player2Iters:
            newResults.append(result)
    return newResults

def analyzeWhere(results, player1Iters, player2Iters):
    player1Wins = 0
    player2Wins = 0
    tiedGames = 0
    games = 0
    totalTurns = 0
    for result in getResultsWhere(results, player1Iters, player2Iters):
        games += 1
        totalTurns += result.gameTurns
        if result.gameResult == 1:
            player1Wins += 1
        elif result.gameResult == 2:
            player2Wins += 1
        else:
            tiedGames += 1
    #print(player1Wins, player2Wins, tiedGames, games, totalTurns)
    print("For " + str(player1Iters) + ":" + str(player2Iters) + " " + str(games) + " games were played, player1 won: " + str(player1Wins) + ", player2 won: " + str(player2Wins) + ", tied games: " + str(tiedGames) + " player1 win rate was: " + str(player1Wins/games) + " tie rate was: " + str(tiedGames/games) + " average turns per game " + str(totalTurns/games))
    return player1Wins/games

def plotValues(results, player1Iters, start, step, stop):
    xValues = []
    yValues = []
    for i in range(start, stop+step, step):
        player1Wins = 0
        games = 0
        for result in getResultsWhere(results, player1Iters, i):
            games += 1
            if result.gameResult == 1:
                player1Wins += 1
        xValues.append(i)
        yValues.append((player1Wins/games)*100)
    print(xValues)
    print(yValues)
    plt.title("Winrate for player 1 with " + str(player1Iters) + " MCTS iterations")
    plt.xlabel("Player 2 MCTS iterations")
    plt.ylabel("Player 1 win rate")
    plt.plot(xValues, yValues)

def plotAverageTurns(results, player1Iters, start, step, stop):
    xValues = []
    yValues = []
    for i in range(start, stop+step, step):
        totalTurns = 0
        games = 0
        for result in getResultsWhere(results, player1Iters, i):
            games += 1
            totalTurns += result.gameTurns 
        xValues.append(i)
        yValues.append((totalTurns/games))
    print(xValues)
    print(yValues)
    plt.title("Average turns per game for player 1 with " + str(player1Iters) + " MCTS iterations")
    plt.xlabel("Player 2 MCTS iterations")
    plt.ylabel("Average turns per game")
    plt.plot(xValues, yValues)

results = []
with open("results.txt", "r") as outputFile:
    lines = outputFile.readlines()
    for line in lines:
        resultArr = line.strip().split(", ")
        #print(resultArr)
        results.append(Result(int(resultArr[0]), int(resultArr[1]), int(resultArr[2]), int(resultArr[3])))
print("Loaded " + str(len(results)) + " game results.")
#analyzeWhere(results, 100, 100)
plt.style.use('ggplot')
#plotValues(results, 150, 25, 25, 550)
plotAverageTurns(results, 150, 25, 25, 550)
plt.show()
