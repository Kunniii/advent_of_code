from p1 import loadFile, log

def solution(inp: list[str]):
    log("debug")
    return inp

if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()