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


def solution(inp: list[str]):
    log("Debug")
    return inp


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
