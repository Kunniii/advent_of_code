from p1 import loadFile, mul
import re

def solution(inp: list[str]):
    pattern = "mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)"
    total = 0
    skip = False
    for line in inp:
        matches = re.findall(pattern, line)
        for match in matches:
            if match == "don't()":
                skip = True
            elif match == "do()":
                skip = False
            print(not skip, match)
            if skip:
                continue
            else:
                if match.startswith('mul'):
                    total += mul(match)
    return total




if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()