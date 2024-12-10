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
    disk_map = inp[0]

    blocks: list[str] = []
    isFile = True
    for i in range(len(disk_map)):
        if isFile:
            file = int(disk_map[i])
            for f in range(1, file+1):
                blocks.append(str(i // 2))
        else:
            free_space = int(disk_map[i])
            blocks += list("." * free_space)
        isFile = not isFile

    len_blocks = len(blocks)
    # log((blocks))

    for i in range(len_blocks):
        if blocks[i] == ".":
            for j in range(len_blocks - 1, i, -1):
                if blocks[j] != ".":
                    t = blocks[i]
                    blocks[i] = blocks[j]
                    blocks[j] = t
                    break
        # log(''.join(blocks), cmd=True)
    # log((blocks))

    total = 0

    for i in range(len_blocks):
        s = blocks[i]
        if s.isnumeric():
            # log(f"Calc {s}*{i}", cmd=True)
            total += int(s) * i
    log(total, cmd=True)
    return total

if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
