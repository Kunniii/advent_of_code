from sys import argv
import re

def loadFile() -> list[str]:
    if len(argv) == 2 and argv[1] == "--test":
        file = open("./input.test.txt", "r", encoding="utf-8")
    else:
        file = open("./input.txt", "r", encoding="utf-8")

    lines = file.read().splitlines()
    file.close()
    return lines

def mul(s: str):
    s = s.replace("mul(", "")
    s = s.replace(")", "")
    a = s.split(",")
    return int(a[0]) * int(a[1])

def solution(inp: list[str]):
    pattern = "mul\\(\\d{1,3},\\d{1,3}\\)"
    regex = re.compile(pattern)
    total = 0

    for line in inp:
        if regex.search(line):
            for s in regex.findall(line):
                total += mul(s)

    return total


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()