from sys import argv
from logger import Logger

logger = Logger()
log = logger.log


def loadFile() -> list[str]:
    if len(argv) == 2 and argv[1] == "--test":
        file = open("./input.test.txt", "r", encoding="utf-8")
    else:
        file = open("./input.txt", "r", encoding="utf-8")

    lines = file.read().splitlines()
    file.close()
    return lines


def try_calc(res: int, inp: str):
    max_bits = inp.strip().count(" ")
    numbers = [int(i) for i in inp.strip().split(" ")]
    number_from_bin = int("1" * max_bits, 2)

    for x in range(number_from_bin + 1):
        op = ["*" if i == "1" else "+" for i in format(x, f"0{max_bits}b")]
        total = numbers[0]
        i = 0
        while True:
            log(numbers[i], end=" ")
            n = numbers[i+1]
            if op:
                match op.pop(0):
                    case "+":
                        log("+", end=" ")
                        total += n
                    case "*":
                        log("*", end=" ")
                        total *= n
            i += 1
            if i >= len(numbers)-1:
                break

        if total == res:
            log(f"Bin: {max_bits} - Oct: {number_from_bin}")
            log(res, inp)
            log(f"OK: {total}")
            return res
    return 0


def solution(inp: list[str]):
    total = 0
    for line in inp:
        i_want_this_result, the_operation = (
            int(line.split(": ")[0]),
            line.split(": ")[1],
        )
        total += try_calc(i_want_this_result, the_operation)
        log()
    return total


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
