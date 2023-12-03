from sys import argv

CONFIG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def loadFile() -> list:
    if len(argv) == 2 and argv[1] == "--test":
        file = open("./input.test.txt", "r", encoding="utf-8")
    else:
        file = open("./input.txt", "r", encoding="utf-8")

    lines = file.read().splitlines()
    file.close()
    return lines


def parseGames(gamesInString: list) -> dict:
    games = {}
    for game in gamesInString:
        part1, part2 = game.split(": ")
        gameId = int(part1.split(" ")[1])
        games[gameId] = []
        rounds = part2.split("; ")
        for r in rounds:
            cubesRevealed = {}
            cubesInText = r.split(", ")
            for cubeNumberName in cubesInText:
                cubeNumber, cubeName = cubeNumberName.split(" ")
                cubesRevealed[cubeName] = int(cubeNumber)
            games[gameId].append(cubesRevealed)
    return games


if __name__ == "__main__":
    inp = loadFile()
    games = parseGames(inp)
    total = 0
    for gameId, rounds in games.items():
        valid = []
        for cubes in rounds:
            for name, amount in cubes.items():
                valid.append(True if amount <= CONFIG.get(name) else False)
        if all(valid):
            total += gameId
    print(total)
