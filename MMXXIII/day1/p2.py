import re


def extractNumber(input: str) -> list:
    regexPattern = (
        r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d)"
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
    for matches in re.findall(regexPattern, input):
        for match in matches:
            if match and match.isdigit():
                numbers.append(match)
            elif match:
                numbers.append(text2number[match])

    return numbers


def get2DigitsNumber(numbers: list) -> int:
    if len(numbers) == 1:
        # the string times 2
        return int(numbers[0] * 2)
    else:
        return int(numbers[0] + numbers[-1])


with open("./input/p2.txt", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()
    numbers = []
    for line in lines:
        numbersInLine = extractNumber(line)
        number = get2DigitsNumber(numbersInLine)
        numbers.append(number)
    print(sum(numbers))
