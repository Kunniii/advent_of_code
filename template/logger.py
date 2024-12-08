class Logger:
    def __init__(self) -> None:
        self.log_file = open("debug.log", "w+")

    def log(self, *objects, sep=" ", end="\n", flush=False):
        print(*objects, sep=sep, end=end, file=self.log_file, flush=flush)

    def __del__(self):
        self.log_file.close()
