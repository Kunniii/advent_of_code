import re
from sys import argv
from p1 import get2DigitsNumber


def extractNumber(input: str) -> list:
    # get all, include the overlaps!
    regexPattern = (
        r"(?=(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d))"
    )

    text2number = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    numbers = []

    # find all matches in the input
    allMatches = re.findall(regexPattern, input)
    print(allMatches)
    for matches in allMatches:
        for match in matches:
            if match and match.isdigit():
                numbers.append(match)
            elif match:
                numbers.append(text2number[match])

    return numbers


if __name__ == "__main__":
    # added option to run test input
    if len(argv) == 2 and argv[1] == "--test":
        file = open("./input.test.txt", "r", encoding="utf-8")
    else:
        file = open("./input.txt", "r", encoding="utf-8")

    lines = file.read().splitlines()
    file.close()
    numbers = []
    with open("debug.log", "w+", encoding="utf-8") as f:
        for line in lines:
            numbersInLine = extractNumber(line)
            number = get2DigitsNumber(numbersInLine)
            numbers.append(number)
            debug = f"{numbersInLine} ** {number}"
            print(debug, file=f)
        total = sum(numbers)
        print(f"\n{total}", file=f)
        print(total)
