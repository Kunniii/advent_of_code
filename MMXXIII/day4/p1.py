from sys import argv


def loadFile() -> list:
    if len(argv) == 2 and argv[1] == "--test":
        file = open("./input.test.txt", "r", encoding="utf-8")
    else:
        file = open("./input.txt", "r", encoding="utf-8")

    lines = file.read().splitlines()
    file.close()
    return lines


def calculatePoint(card: str) -> int:
    point = 0
    cardValues = card.split(":")[1]
    winningNumbers, myNumbers = cardValues.split("|")
    winningNumbers = winningNumbers.split()
    myNumbers = myNumbers.split()
    for number in winningNumbers:
        if number in myNumbers:
            point = point + 1 if point == 0 else point * 2
    return point


if __name__ == "__main__":
    inp = loadFile()
    total = 0
    for card in inp:
        point = calculatePoint(card)
        total += point
    print(total)
