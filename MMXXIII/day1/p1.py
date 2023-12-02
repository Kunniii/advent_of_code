def extractNumber(input: str) -> list:
    numbers = []
    for letter in input:
        # i can also check the ascii value!
        # or, use Regex!!!
        if letter.isdigit():
            # keep this as string for easy concat
            numbers.append(letter)

    return numbers


def get2DigitsNumber(numbers: list) -> int:
    if len(numbers) == 1:
        # the string times 2
        return int(numbers[0] * 2)
    else:
        return int(numbers[0] + numbers[-1])


if __name__ == "__main__":
    with open("./input/p1.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
        numbers = []
        listOfNumbers = []
        for line in lines:
            numbersInLine = extractNumber(line)
            listOfNumbers.append(numbersInLine)
            number = get2DigitsNumber(numbersInLine)
            numbers.append(number)
        print(sum(numbers))

    with open("p1.out.txt", "w+", encoding="utf-8") as f:
        for i in listOfNumbers:
            print(i, file=f)
