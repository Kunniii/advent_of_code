from p1 import loadFile, parseGames

if __name__ == "__main__":
    inp = loadFile()
    games = parseGames(inp)

    total = 0
    for gameId, rounds in games.items():
        maxR = 0
        maxG = 0
        maxB = 0
        for cubes in rounds:
            R = cubes.get("red")
            G = cubes.get("green")
            B = cubes.get("blue")

            maxR = R if R and R > maxR else maxR
            maxG = G if G and G > maxG else maxG
            maxB = B if B and B > maxB else maxB
        total += maxR * maxG * maxB
    print(total)
