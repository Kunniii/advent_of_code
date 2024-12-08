from p1 import loadFile, log, how_to_go_from_a_to_b, Node
import itertools


def solution(inp: list[str]):
    H, W = len(inp), len(inp[0])
    nodes_map: dict[str, list[Node]] = {}

    board = [list(i) for i in inp]

    for y in range(H):
        for x in range(W):
            c = inp[y][x]
            if c not in [".", "#"]:
                node_with_type = nodes_map.get(c, [])
                node_with_type.append(Node(x, y))
                nodes_map[c] = node_with_type

    total = 0

    for nodes in nodes_map.values():
        log(nodes)
        for [nodeA, nodeB] in itertools.product(nodes, repeat=2):
            if nodeA == nodeB:
                continue
            (x, y) = how_to_go_from_a_to_b(nodeA, nodeB)
            i = 2
            while True:
                (x2, y2) = nodeA.apply(x * i, y * i)
                if 0 <= x2 < W and 0 <= y2 < H:
                    log(f"OK {x2}, {y2} - {W}, {H}")
                    if board[y2][x2] == ".":
                        board[y2][x2] = "#"
                    i += 1
                else:
                    log(f"NOT {x2}, {y2} - {W}, {H}")
                    break

    log()

    for line in board:
        log("".join(line))
        total += line.count("#")

    for nodes in nodes_map.values():
        total += len(nodes) if len(nodes) > 1 else 0

    return total


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
