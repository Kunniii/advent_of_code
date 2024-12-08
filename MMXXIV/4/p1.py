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
    h = len(inp)
    w = len(inp[0])
    max_h = h - 3
    max_w = w - 3

    total_h = 0
    for line in inp:
        total_h += line.count("XMAS")
        total_h += line.count("SAMX")

    log(total_h)
    
    total_v = 0
    for i in range(max_h):
        i1, i2, i3 = i + 1, i + 2, i + 3
        for j in range(w):
            s = inp[i][j] + inp[i1][j] + inp[i2][j] + inp[i3][j]
            if s in ["SAMX", "XMAS"]:
                total_v +=1
    log(total_v)


    total_xr = 0
    for i in range(max_h):
        i1, i2, i3 = i + 1, i + 2, i + 3
        for j in range(max_w):
            j1, j2, j3 = j + 1, j + 2, j + 3
            sx = inp[i][j] + inp[i1][j1] + inp[i2][j2] + inp[i3][j3]

            if sx in ["SAMX", "XMAS"]:
                log(j+1, i+1)
                total_xr += 1

    log(total_xr)

    total_lr = 0
    for i in range(max_h):
        i1, i2, i3 = i + 1, i + 2, i + 3
        for j in range(w - 1, 2,  -1):
            j1, j2, j3 = j - 1, j - 2, j - 3
            sx = inp[i][j] + inp[i1][j1] + inp[i2][j2] + inp[i3][j3]
            if sx in ["SAMX", "XMAS"]:
                log(j+1, i+1)
                total_lr += 1
        log()
    log(total_lr)

    return total_lr + total_xr + total_h + total_v


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
