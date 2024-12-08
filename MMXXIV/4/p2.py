from p1 import loadFile, log


class Matrix:
    data: list[str]

    def __init__(self, data: list[str]):
        self.data = data

    def equals(self, other: "Matrix"):
        mr0 = self.data[0]
        mr1 = self.data[1]
        mr2 = self.data[2]

        or0 = other.data[0]
        or1 = other.data[1]
        or2 = other.data[2]

        checks = [
            mr0[0] == or0[0],
            mr0[2] == or0[2],
            mr1[1] == or1[1],
            mr2[0] == or2[0],
            mr2[2] == or2[2],
        ]

        return all(checks)

    def __repr__(self):
        return str(f"{self.data[0]}\n{self.data[1]}\n{self.data[2]}\n")

S1 = Matrix(
    [
        "M.M",
        ".A.",
        "S.S",
    ]
)

S2 = Matrix(
    [
        "S.M",
        ".A.",
        "S.M",
    ]
)

S3 = Matrix(
    [
        "S.S",
        ".A.",
        "M.M",
    ]
)

S4 = Matrix(
    [
        "M.S",
        ".A.",
        "M.S",
    ]
)


def solution(inp: list[str]):
    total = 0
    for i in range(len(inp) - 2):
        i1, i2 = i + 1, i + 2
        for j in range(len(inp[0]) - 2):
            j2 = j + 3
            m = Matrix([inp[i][j:j2], inp[i1][j:j2], inp[i2][j:j2]])
            res = [
                m.equals(S1),
                m.equals(S2),
                m.equals(S3),
                m.equals(S4),
            ]
            if any(res):
                total += res.count(True)
                log(m)
    return total


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
