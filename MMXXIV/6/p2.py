from p1 import loadFile, log, Board, Guard


class GuardInMatrix(Guard):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)
        self.history_routes = set()

    def move_in_matrix(self):
        while self.faces_obstacle():
            self.turn()
        self.x, self.y = self.get_new_pos()
        if (self.accelerate, (self.x, self.y)) in self.history_routes:
            return "it must be a loop"

        self.history_routes.add((self.accelerate, (self.x, self.y)))
        self.board.visit(self.x, self.y)

    def give_me_your_history_routes(self):
        return self.history_routes


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
    guard = Guard(guard_x, guard_y, board)

    while guard.can_move():
        guard.move()

    total = 0

    visited_pos = board.visited_pos.copy()

    for x, y in visited_pos:
        matrix_obstacles = obstacles.copy()
        matrix_obstacles.append((x, y))
        the_matrix = Board(w, h, matrix_obstacles)
        guard_in_the_matrix = GuardInMatrix(guard_x, guard_y, the_matrix)
        while guard_in_the_matrix.can_move():
            what_the_guard_thinks = guard_in_the_matrix.move_in_matrix()
            if what_the_guard_thinks == "it must be a loop":
                total += 1
                print(total)
                log(f"Valid obstacle at: {x}:{y}")
                break

    return total


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
