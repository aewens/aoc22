from pprint import pprint

class CPU:
    def __init__(self):
        self.x = 1
        self.v = None
        self.during = 1
        self.after = 1

        self.cycle = 0
        self.waiting = True
        self.resume = 0

        self.sprite = [0,1,2]
        self.cursor = 0
        self.row = 0
        self.width = 40
        self.crt = dict()

    def load(self, line):
        self.waiting = False
        if line == "noop":
            self.resume = 1
            return

        self.v = int(line.split(" ", 1)[1])
        self.resume = 2

    def tick(self):
        self.cycle = self.cycle + 1
        self.resume = self.resume - 1
        if self.resume == 0:
            self.waiting = True

        self.during = self.x
        self.sprite = [self.x-1, self.x, self.x+1]

        position = self.cursor + self.row * self.width
        self.crt[position] = self.cursor in self.sprite

        if self.v is not None and self.waiting:
            self.after = self.x + self.v
            self.v = None
            self.x = self.after

        self.cursor = (self.cursor + 1) % self.width
        if self.cursor == 0:
            self.row = self.row + 1

    def display(self):
        h = 6
        w = 40
        for y in range(h):
            row = ""
            for x in range(w):
                pixel = "#" if self.crt[w*y+x] else " "
                row = row + pixel

            print(row)

    def __repr__(self):
        return f"CPU({self.cycle}, {self.during}, {self.after})"

def p1(puzzle_input, simple=False):
    results = dict()
    checks = [220, 180, 140, 100, 60]
    check = 20

    cpu = CPU()
    for line in puzzle_input:
        if cpu.waiting:
            cpu.load(line)

        while not cpu.waiting:
            cpu.tick()
            if not simple and cpu.cycle == check:
                results[check] = cpu.cycle * cpu.during
                if len(checks) > 0:
                    check = checks.pop()

    return cpu.x if simple else sum(results.values())

def p2(puzzle_input):
    cpu = CPU()
    for line in puzzle_input:
        if cpu.waiting:
            cpu.load(line)

        while not cpu.waiting:
            cpu.tick()

    cpu.display()
    return None

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
