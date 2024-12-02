from p1 import loadFile


def try_to_make_safe(array: list[int]):
    index = list(range(len(array)))
    for i in index:
        arr = array.copy()
        del arr[i]
        safe = check_safe(arr)
        if safe:
            return True
    return False


def check_safe(array: list[int]):
    ok = []
    print(f"Check {array}")
    flow = (array[0] - array[1]) > 0

    for n in range(len(array) - 1):
        if ((array[n] - array[n + 1]) > 0) == flow:
            ok.append(1 <= abs(array[n] - array[n + 1]) <= 3)
        else:
            ok.append(False)
            break
    return all(ok)


def solution(inp: list[str]):
    safes = 0
    for line in inp:
        array = list(map(int, line.split()))
        if check_safe(array):
            safes += 1
        elif try_to_make_safe(array):
            safes += 1
    return safes


if __name__ == "__main__":
    inp = loadFile()
    print(solution(inp))
