from p1 import loadFile, up, down, left, right, expandToGetNumber


def createMatrix(inp) -> tuple[list, list]:
    matrix = []
    for line in inp:
        matrix.append(list(line))

    symbolPos = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            char = matrix[row][col]
            if char != "." and not char.isdigit() and char == "*":
                symbolPos.append((row, col))

    return (matrix, symbolPos)


if __name__ == "__main__":
    inp = loadFile()
    matrix, gearPos = createMatrix(inp)
    alreadyIncludedPos = []
    total = 0

    for pos in gearPos:
        adjNumbers = []
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
        row, col = pos
        if len(adjNumbers) == 2:
            total += adjNumbers[0] * adjNumbers[1]
        elif len(adjNumbers) > 2:
            raise "OHNO"
    print(total)
