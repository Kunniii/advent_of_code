from sys import argv

def loadFile() -> list[list[str]]:
    if len(argv) == 2 and argv[1] == "--test":
        file = open("./input.test.txt", "r", encoding="utf-8")
    else:
        file = open("./input.txt", "r", encoding="utf-8")

    lines = file.read()
    
    [p1, p2] = lines.split("\n\n")

    file.close()

    return [p1.split("\n"), p2.split("\n")]

def solution(inp: list[list[str]]):
    res = []
    p1, p2 = inp[0], inp[1]
    violate = []
    for s in p1:
        [a, b] = s.split('|')
        violate.append((int(b), int(a)))
    arr: list[list[int]] = []
    for s in p2:
        o: list[int] = []
        for x in s.split(','):
            o.append(int(x))
        arr.append(o)

    for numbers in arr:
        ok = True
        for i, n in enumerate(numbers):
            for j in range(i + 1, len(numbers)):
                if violate.count((n, numbers[j])):
                    print((n, numbers[j]))
                    ok = False
        if ok:
            res.append(numbers)
            print()
    total = 0
    for r in res:
        mid = len(r) // 2
        num_mid = r[mid]
        total += num_mid
    print(total)
    
    return total

if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()