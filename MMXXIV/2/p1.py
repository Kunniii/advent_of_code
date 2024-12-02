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
    safes = 0
    for line in inp:
        arr = list(map(int, line.split()))
        ok = []
        print(f"Check {line}")
        flow = (arr[0] - arr[1]) > 0
        print(f'Flow {flow} {"DOWN" if flow else "UP"}')

        for n in range(len(arr) - 1):
            if ((arr[n] - arr[n + 1]) > 0) == flow:
                ok.append(1 <= abs(arr[n] - arr[n + 1]) <= 3)
            else:
                ok.append(False)
                break
        print(ok)
        if all(ok):
            print(f"OK {line}")
            safes += 1

    return safes


if __name__ == "__main__":
    inp = loadFile()
    print(solution(inp))
