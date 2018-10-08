class Result:
    def __init__(self, player1Iters, player2Iters, gameResult, gameTurns):
        self.player1Iters = player1Iters
        self.player2Iters = player2Iters
        self.gameResult = gameResult
        self.gameTurns = gameTurns

def analyzeWhere(results, player1Iters, player2Iters):
    player1Wins = 0
    player2Wins = 0
    tiedGames = 0
    games = 0
    totalTurns = 0
    for result in results:
        if result.player1Iters == player1Iters and result.player2Iters == player2Iters:
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

results = []
with open("results.txt", "r") as outputFile:
    lines = outputFile.readlines()
    for line in lines:
        resultArr = line.strip().split(", ")
        #print(resultArr)
        results.append(Result(int(resultArr[0]), int(resultArr[1]), int(resultArr[2]), int(resultArr[3])))
print("Loaded " + str(len(results)) + " game results.")
analyzeWhere(results, 100, 100)
