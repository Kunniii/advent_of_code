from sys import argv

def loadFile() -> list[str]:
    if len(argv) == 2 and argv[1] == "--test":
        file = open("./input.test.txt", "r", encoding="utf-8")
    else:
        file = open("./input.txt", "r", encoding="utf-8")

    lines = file.read().splitlines()
    file.close()
    return lines


def solution(inp: list[str]):
    left = []
    right = []
    for line in inp:
        leftNum, rightNum = map(int, line.strip().split())
        left.append(leftNum)
        right.append(rightNum)
    left.sort()
    right.sort()
    
    total_dis = 0
    
    for i in range(len(inp)):
        total_dis += abs(left[i] - right[i])
    
    return total_dis


if __name__ == "__main__":
    inp = loadFile()
    print(solution(inp))