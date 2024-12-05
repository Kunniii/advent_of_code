from p1 import loadFile

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
        if not ok:
            res.append(numbers)
            print(numbers)
            print()
    total = 0
    for r in res:
        ok = False
        

        while not ok:
            ok = True
            for i in range(len(r)-1):
                for j in range(i + 1, len(r)):
                    if violate.count((r[i], r[j])):
                        t = r[i]
                        r[i] = r[j]
                        r[j] = t
                        ok = False
            print(r)
                
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