from p1 import loadFile, log


def ternary(n: int, pad=0):
    if n == 0:
        return "0".rjust(pad, "0")
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return "".join(reversed(nums)).rjust(pad, "0")


def try_calc(res: int, inp: str):
    max_bits = inp.strip().count(" ")
    numbers = [int(i) for i in inp.strip().split(" ")]
    max_iter = int("2" * max_bits, 3)
    for x in range(max_iter + 1):
        op = []
        for i in ternary(x, max_bits):
            match i:
                case "0":
                    op.append("*")
                case "1":
                    op.append("+")
                case "2":
                    op.append("||")

        total = numbers[0]
        i = 0
        op_cp = op.copy()

        while True:
            n = numbers[i + 1]
            if op:
                match op.pop(0):
                    case "+":
                        total += n
                    case "*":
                        total *= n
                    case "||":
                        total = int(str(total) + str(n))
            i += 1
            if i >= len(numbers) - 1:
                break

        if total == res:
            log(f"Bin: {max_bits} - Oct: {max_iter}")
            log(res, inp, op_cp)
            log(f"OK: {total}")
            return res
    return 0


def solution(inp: list[str]):
    total = 0
    for line in inp:
        i_want_this_result, the_operation = (
            int(line.split(": ")[0]),
            line.split(": ")[1],
        )
        total += try_calc(i_want_this_result, the_operation)
        log()
    return total


if __name__ == "__main__":
    inp = loadFile()
    fh = open("output.txt", "w+")
    fh.write(str(solution(inp)))
    fh.close()
