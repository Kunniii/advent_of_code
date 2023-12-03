from sys import argv

UP = (0, -1)
DOWN = (0, +1)
LEFT = (-1, 0)
RIGHT = (+1, 0)


def loadFile() -> list:
    if len(argv) == 2 and argv[1] == "--test":
        file = open("./input.test.txt", "r", encoding="utf-8")
    else:
        file = open("./input.txt", "r", encoding="utf-8")

    lines = file.read().splitlines()
    file.close()
    return lines


def createMatrix(inp) -> tuple[list, list]:
    matrix = []
    for line in inp:
        matrix.append(list(line))

    symbolPos = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            char = matrix[x][y]
            if char != "." and not char.isdigit():
                symbolPos.append((x, y))

    return (matrix, symbolPos)


def expandToGetNumber(line: list, contactIndex: tuple) -> tuple[int, tuple]:
    nStart = 0
    nEnd = 0

    # move backward
    x, _ = contactIndex
    while x >= 0:
        if x == 0:
            nStart = x
            break
        if line[x].isdigit():
            x -= 1
            continue
        if line[x] == ".":
            nStart = x + 1
            break

    # move forward
    x, _ = contactIndex
    while True:
        if x == len(line):
            nEnd = x
            break
        if line[x].isdigit():
            x += 1
            continue
        if line[x] == ".":
            nEnd = x - 1
            break
    nEnd += 1

    n = "".join(line[nStart:nEnd])

    return int(n), (nStart, nEnd)


if __name__ == "__main__":
    inp = loadFile()
    matrix, symbolPos = createMatrix(inp)
    alreadyIncludedPos = []
    """
    for each symbol's pos, move:
        UP until y=0
        DOWN until y=max
        LEFT until x=0
        RIGHT until x=max
        if any move hit a digit:
            if it is not in already:
                get x, y = contactIndex
                perform number, start, end = expand()
                for i in range(start, end+1):
                    already.append((i, y))
                total += number
    """
