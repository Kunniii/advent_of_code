from sys import argv


def loadFile() -> list:
    if "--test" in argv:
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
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            char = matrix[row][col]
            if char != "." and not char.isdigit():
                symbolPos.append((row, col))

    return (matrix, symbolPos)


def expandToGetNumber(line: list, contactIndex: tuple) -> tuple[int, tuple]:
    nStart = 0
    nEnd = 0

    # move backward
    _, col = contactIndex
    while col >= 0:
        col -= 1
        if not line[col].isdigit():
            nStart = col + 1
            break
        if col == 0:
            nStart = col
            break

    # move forward
    _, col = contactIndex
    while True:
        col += 1
        if not line[col].isdigit():
            nEnd = col - 1
            break
        if col == len(line) - 1:
            nEnd = col
            break
    nEnd += 1

    n = "".join(line[nStart:nEnd])
    return int(n), (nStart, nEnd)


def up(row, col):
    return row - 1, col


def down(row, col):
    return row + 1, col


def left(row, col):
    return row, col - 1


def right(row, col):
    return row, col + 1


if __name__ == "__main__":
    inp = loadFile()
    matrix, symbolPos = createMatrix(inp)
    alreadyIncludedPos = []
    adjNumbers = []
    for pos in symbolPos:
        # UP
        row, col = pos
        if row > 0:
            row, col = up(row, col)
            valueToCheck = matrix[row][col]
            if valueToCheck.isdigit() and not (row, col) in alreadyIncludedPos:
                line = matrix[row]
                contactIndex = (row, col)
                number, (start, end) = expandToGetNumber(line, contactIndex)
                adjNumbers.append(number)

                for i in range(start, end):
                    alreadyIncludedPos.append((row, i))

        # DOWN
        row, col = pos
        if row < len(matrix) - 1:
            row, col = down(row, col)
            valueToCheck = matrix[row][col]
            if valueToCheck.isdigit() and not (row, col) in alreadyIncludedPos:
                line = matrix[row]
                contactIndex = (row, col)
                number, (start, end) = expandToGetNumber(line, contactIndex)
                adjNumbers.append(number)

                for i in range(start, end):
                    alreadyIncludedPos.append((row, i))

        # LEFT
        row, col = pos
        if col > 0:
            row, col = left(row, col)
            valueToCheck = matrix[row][col]
            if valueToCheck.isdigit() and not (row, col) in alreadyIncludedPos:
                line = matrix[row]
                contactIndex = (row, col)
                number, (start, end) = expandToGetNumber(line, contactIndex)
                adjNumbers.append(number)

                for i in range(start, end):
                    alreadyIncludedPos.append((row, i))

        # RIGHT
        row, col = pos
        if col < len(matrix[row]) - 1:
            row, col = right(row, col)
            valueToCheck = matrix[row][col]
            if valueToCheck.isdigit() and not (row, col) in alreadyIncludedPos:
                line = matrix[row]
                contactIndex = (row, col)
                number, (start, end) = expandToGetNumber(line, contactIndex)
                adjNumbers.append(number)

                for i in range(start, end):
                    alreadyIncludedPos.append((row, i))

        # UP LEFT
        row, col = pos
        if row > 0 and col > 0:
            row, col = up(row, col)
            row, col = left(row, col)
            valueToCheck = matrix[row][col]
            if valueToCheck.isdigit() and not (row, col) in alreadyIncludedPos:
                line = matrix[row]
                contactIndex = (row, col)
                number, (start, end) = expandToGetNumber(line, contactIndex)
                adjNumbers.append(number)

                for i in range(start, end):
                    alreadyIncludedPos.append((row, i))

        # UP RIGHT
        row, col = pos
        if row > 0 and col < len(matrix[row]) - 1:
            row, col = up(row, col)
            row, col = right(row, col)
            valueToCheck = matrix[row][col]
            if valueToCheck.isdigit() and not (row, col) in alreadyIncludedPos:
                line = matrix[row]
                contactIndex = (row, col)
                number, (start, end) = expandToGetNumber(line, contactIndex)
                adjNumbers.append(number)

                for i in range(start, end):
                    alreadyIncludedPos.append((row, i))

        # DOWN LEFT
        row, col = pos
        if row < len(matrix) - 1 and col > 0:
            row, col = down(row, col)
            row, col = left(row, col)
            valueToCheck = matrix[row][col]
            if valueToCheck.isdigit() and not (row, col) in alreadyIncludedPos:
                line = matrix[row]
                contactIndex = (row, col)
                number, (start, end) = expandToGetNumber(line, contactIndex)
                adjNumbers.append(number)

                for i in range(start, end):
                    alreadyIncludedPos.append((row, i))

        # DOWN RIGHT
        row, col = pos
        if row < len(matrix) - 1 and col < len(matrix[row]) - 1:
            row, col = down(row, col)
            row, col = right(row, col)
            valueToCheck = matrix[row][col]
            if valueToCheck.isdigit() and not (row, col) in alreadyIncludedPos:
                line = matrix[row]
                contactIndex = (row, col)
                number, (start, end) = expandToGetNumber(line, contactIndex)
                adjNumbers.append(number)

                for i in range(start, end):
                    alreadyIncludedPos.append((row, i))

    print(adjNumbers)
    print(sum(adjNumbers))
