from sys import argv
from logger import Logger
import itertools

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


class Node:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def location(self):
        return (self.x, self.y)

    def apply(self, x: int, y: int):
        return (self.x + x, self.y + y)

    def __repr__(self):
        return f"(x,y)=({self.x},{self.y})"


def how_to_go_from_a_to_b(a: Node, b: Node):
    x1, y1 = a.location()
    x2, y2 = b.location()
    return (x2 - x1, y2 - y1)


def solution(inp: list[str]):
    H, W = len(inp), len(inp[0])
    nodes_map: dict[str, list[Node]] = {}

    board = [list(i) for i in inp]

    for y in range(H):
        for x in range(W):
            c = inp[y][x]
            if c != ".":
                node_with_type = nodes_map.get(c, [])
                node_with_type.append(Node(x, y))
                nodes_map[c] = node_with_type

    # anti_nodes: set[tuple[int, int]] = set()

    total = 0

    for nodes in nodes_map.values():
        for [nodeA, nodeB] in itertools.product(nodes, repeat=2):
            if nodeA == nodeB:
                continue
            (x, y) = how_to_go_from_a_to_b(nodeA, nodeB)
            (x2, y2) = nodeA.apply(x * 2, y * 2)
            if 0 <= x2 < W and 0 <= y2 < H:
                log(f"OK {x2}, {y2} - {W}, {H}")
                board[y2][x2] = "#"
            else:
                log(f"NOT {x2}, {y2} - {W}, {H}")

    log()

    for line in board:
        log("".join(line))
        total += line.count("#")

    # for nodes in nodes_map.values():
    #     for node in nodes:
    #         anti_nodes.discard(node.location())

    # return len(anti_nodes)

    return total


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
