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


class AsciiChar:
    def __init__(self, char: str) -> None:
        self.char = char

    def __sub__(self, other: "AsciiChar") -> str:
        n1 = ord(self.char)
        n2 = ord(other.char)
        if n1 - n2 != 0:
            return "."
        else:
            return "0"


class AsciiStr:
    def __init__(self, str: str) -> None:
        self.str = str

    def __sub__(self, other: "AsciiStr") -> str:
        res = ""
        for c1, c2 in zip(self.str, other.str):
            res += str(AsciiChar(c1) - AsciiChar(c2))
        return res

    def __repr__(self) -> str:
        return self.str


def solution(inp: list[str]):
    total = 0
    # # horizontal
    # for line in inp:
    #     total += line.count("XMAS")
    #     total += line.count("SAMX")

    # for i in range(len(inp)):
    #     s = ""
    #     for j in range(len(inp[i])):
    #         s += inp[j][i]
    #     total += s.count("XMAS")
    #     total += s.count("SAMX")

    stamp = "XMAS"
    revStamp = "SAMX"
    ok = "0000"

    stampTL = ["X...", ".M..", "..A.", "...S"]
    revStampTL = stampTL[::-1]
    stampTR = ["...X", "..M.", ".A..", "S..."]
    revStampTR = stampTR[::-1]

    okTL = ["0...", ".0..", "..0.", "...0"]
    revOKTL = okTL[::-1]
    okTR = ["...0", "..0.", ".0..", "0..."]
    revOKTR = okTR[::-1]

    for i in range(len(inp) - 4):
        for j in range(len(inp[i]) - 4):
            
            sl1 = inp[i][j : j + 4]
            sl2 = inp[i + 1][j : j + 4]
            sl3 = inp[i + 2][j : j + 4]
            sl4 = inp[i + 3][j : j + 4]
            
            l1 = AsciiStr(sl1)
            l2 = AsciiStr(sl2)
            l3 = AsciiStr(sl3)
            l4 = AsciiStr(sl4)
            
            resH1 = AsciiStr(stamp) - l1
            resH2 = AsciiStr(stamp) - l2
            resH3 = AsciiStr(stamp) - l3
            resH4 = AsciiStr(stamp) - l4
            
            resRevH1 = AsciiStr(revStamp) - l1
            resRevH2 = AsciiStr(revStamp) - l2
            resRevH3 = AsciiStr(revStamp) - l3
            resRevH4 = AsciiStr(revStamp) - l4
            
            vS1 = AsciiStr(sl1[0]+sl2[0]+sl3[0]+sl4[0])
            vS2 = AsciiStr(sl1[1]+sl2[1]+sl3[1]+sl4[1])
            vS3 = AsciiStr(sl1[2]+sl2[2]+sl3[2]+sl4[2])
            vS4 = AsciiStr(sl1[3]+sl2[3]+sl3[3]+sl4[3])
            
            resV1 = AsciiStr(stamp) - vS1
            resV2 = AsciiStr(stamp) - vS2
            resV3 = AsciiStr(stamp) - vS3
            resV4 = AsciiStr(stamp) - vS4
            
            resRevV1 = AsciiStr(revStamp) - vS1
            resRevV2 = AsciiStr(revStamp) - vS2
            resRevV3 = AsciiStr(revStamp) - vS3
            resRevV4 = AsciiStr(revStamp) - vS4

            res1TL = AsciiStr(stampTL[0]) - l1
            res2TL = AsciiStr(stampTL[1]) - l2
            res3TL = AsciiStr(stampTL[2]) - l3
            res4TL = AsciiStr(stampTL[3]) - l4

            res1TR = AsciiStr(stampTR[0]) - l1
            res2TR = AsciiStr(stampTR[1]) - l2
            res3TR = AsciiStr(stampTR[2]) - l3
            res4TR = AsciiStr(stampTR[3]) - l4

            resRev1TL = AsciiStr(revStampTL[0]) - l1
            resRev2TL = AsciiStr(revStampTL[1]) - l2
            resRev3TL = AsciiStr(revStampTL[2]) - l3
            resRev4TL = AsciiStr(revStampTL[3]) - l4

            resRev1TR = AsciiStr(revStampTR[0]) - l1
            resRev2TR = AsciiStr(revStampTR[1]) - l2
            resRev3TR = AsciiStr(revStampTR[2]) - l3
            resRev4TR = AsciiStr(revStampTR[3]) - l4

            resTL = [res1TL, res2TL, res3TL, res4TL]
            resTR = [res1TR, res2TR, res3TR, res4TR]
            resRevTL = [resRev1TL, resRev2TL, resRev3TL, resRev4TL]
            resRevTR = [resRev1TR, resRev2TR, resRev3TR, resRev4TR]

            if resH1 == ok:
                total += 1
                log(stamp)
                log("\n----\n")
            if resH2 == ok:
                total += 1
                log(stamp)
                log("\n----\n")
            if resH3 == ok:
                total += 1
                log(stamp)
                log("\n----\n")
            if resH4 == ok:
                total += 1
                log(stamp)
                log("\n----\n")
            
            if resRevH1 == ok:
                total += 1
                log(revStamp)
                log("\n----\n")
            if resRevH2 == ok:
                total += 1
                log(revStamp)
                log("\n----\n")
            if resRevH3 == ok:
                total += 1
                log(revStamp)
                log("\n----\n")
            if resRevH4 == ok:
                total += 1
                log(revStamp)
                log("\n----\n")

            if resV1 == ok:
                total += 1
                log(vS1)
                log("\n----\n")
            if resV2 == ok:
                total += 1
                log(vS2)
                log("\n----\n")
            if resV3 == ok:
                total += 1
                log(vS3)
                log("\n----\n")
            if resV4 == ok:
                total += 1
                log(vS4)
                log("\n----\n")

            if resRevV1 == ok:
                total += 1
                log(revStamp)
                log("\n----\n")
            if resRevV2 == ok:
                total += 1
                log(revStamp)
                log("\n----\n")
            if resRevV3 == ok:
                total += 1
                log(revStamp)
                log("\n----\n")
            if resRevV4 == ok:
                total += 1
                log(revStamp)
                log("\n----\n")
            
            if resTL == okTL:
                total += 1
                log(stampTL[0])
                log(stampTL[1])
                log(stampTL[2])
                log(stampTL[3])
                log("\n----\n")
            if resTR == okTR:
                total += 1
                log(stampTR[0])
                log(stampTR[1])
                log(stampTR[2])
                log(stampTR[3])
                log("\n----\n")
            if resRevTL == revOKTL:
                total += 1
                log(revStampTL[0])
                log(revStampTL[1])
                log(revStampTL[2])
                log(revStampTL[3])
                log("\n----\n")
            if resRevTR == revOKTR:
                total += 1
                log(revStampTR[0])
                log(revStampTR[1])
                log(revStampTR[2])
                log(revStampTR[3])
                log("\n----\n")
    return total


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
