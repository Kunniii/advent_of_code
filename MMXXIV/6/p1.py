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


class Board:
    obstacles: list[tuple[int, int]]
    matrix: list[list]
    w: int
    h: int

    def __init__(self, w: int, h: int, obstacles: list[tuple[int, int]]):
        self.w, self.h = w, h
        self.matrix = [list("." * w) for _ in range(h)]

        self.obstacles = obstacles
        for o in obstacles:
            self.matrix[o[0]][o[1]] = "#"

    def __repr__(self):
        s = ""
        for i in self.matrix:
            s += "".join(i) + "\n"
        return s

    def visit(self, x: int, y: int):
        self.matrix[x][y] = "X"

    def visited(self):
        s = 0
        for i in self.matrix:
            s += i.count("X")
        return s


class Guard:
    def __init__(self, x: int, y: int, board: Board):
        self.board = board
        self.x, self.y = x, y
        self.board.visit(x, y)

        self.directions = {
            "UP": (-1, 0),
            "DOWN": (+1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, +1),
        }
        self.accelerate = "UP"

    def turn(self) -> None:
        match self.accelerate:
            case "UP":
                self.accelerate = "RIGHT"
            case "RIGHT":
                self.accelerate = "DOWN"
            case "DOWN":
                self.accelerate = "LEFT"
            case "LEFT":
                self.accelerate = "UP"

    def can_move(self):
        x, y = self.get_new_pos()
        match self.accelerate:
            case "UP":
                return x >= 0
            case "DOWN":
                return x < self.board.h
            case "LEFT":
                return  y >= 0
            case "RIGHT":
                return y < self.board.w


    def get_new_pos(self):
        new_x = self.x + self.directions.get(self.accelerate)[0]
        new_y = self.y + self.directions.get(self.accelerate)[1]
        return (new_x, new_y)

    def faces_obstacle(self):
        new_x, new_y = self.get_new_pos()
        return (new_x, new_y) in self.board.obstacles

    def move(self):
        log(f"Current: {self.x, self.y}")
        while self.faces_obstacle():
            log(f"Faces obstacle at {self.get_new_pos()}")
            self.turn()
        self.x, self.y = self.get_new_pos()
        self.board.visit(self.x, self.y)
        log(f"Moved {self.accelerate} at {self.get_new_pos()}")


def solution(inp: list[str]):
    h, w = len(inp), len(inp[0])
    guard_x: int
    guard_y: int
    obstacles = []

    for x in range(h):
        for y in range(w):
            if inp[x][y] == "^":
                guard_x, guard_y = x, y
            if inp[x][y] == "#":
                obstacles.append((x, y))

    board = Board(w, h, obstacles)
    log(board)
    guard = Guard(guard_x, guard_y, board)

    while guard.can_move():
        guard.move()

    log(board)

    return board.visited()


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
