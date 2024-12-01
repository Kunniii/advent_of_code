from p1 import loadFile

def solution(inp: list[str]):
    left = []
    right = []
    for line in inp:
        leftNum, rightNum = map(int, line.strip().split())
        left.append(leftNum)
        right.append(rightNum)
    
    total_dis = 0
    
    for i in left:
        print(f"{i} {right.count(i)}")
        total_dis += i*right.count(i)

    return total_dis

if __name__ == "__main__":
    inp = loadFile()
    print(solution(inp))