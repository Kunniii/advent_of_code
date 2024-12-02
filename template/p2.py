from p1 import loadFile

def solution(inp: list[str]):
    return inp

if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()