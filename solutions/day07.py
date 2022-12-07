from pprint import pprint

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name):
        self.name = name
        self.entries = dict()
        self.dirs = dict()
        self.files = dict()

        self.parent = None
        self.size = None

    def add_dir(self, name):
        entry = Dir(name)
        entry.parent = self
        self.dirs[name] = entry
        self.entries[name] = entry
        return entry

    def add_file(self, name, size):
        entry = File(name, size)
        self.files[name] = entry
        self.entries[name] = entry
        return entry

    def up(self):
        return self.parent

    def cd(self, name):
        return self.dirs[name]

    def compute(self):
        if self.size is not None:
            return self.size

        total = sum(f.size for f in self.files.values())
        for entry in self.dirs.values():
            total = total + entry.compute()

        self.size = total
        return total

def walk(pointer, cap):
    if isinstance(pointer, int):
        return 0 if pointer > cap else pointer

    total = 0 if pointer.size > cap else pointer.size
    for value in pointer.dirs.values():
        total = total + walk(value, cap)

    return total

def collect(pointer, path, sizes):
    for key, value in pointer.dirs.items():
        route = "".join(path + [key])
        sizes[route] = collect(value, path + [key], sizes)

    return pointer.size

def build(puzzle_input):
    root = Dir("/")
    pointer = None
    for line in puzzle_input:
        if line.startswith("$"):
            cmd = line[2:].split()
            if cmd[0] == "cd":
                route = cmd[1]
                if route == "/":
                    pointer = root
                    continue

                if route == "..":
                    pointer = pointer.parent
                    continue

                pointer = pointer.cd(route)
                continue

            if cmd[0] == "ls":
                continue

        fst, snd = line.split(" ", 1)
        if fst == "dir":
            pointer.add_dir(snd)
            continue

        size = int(fst)
        pointer.add_file(snd, size)

    root.compute()
    return root

def p1(puzzle_input):
    root = build(puzzle_input)
    return walk(root, 100000)

def p2(puzzle_input):
    root = build(puzzle_input)
    maxsize = 70000000
    needed = 30000000
    unused = maxsize - root.size

    sizes = dict()
    sizes["/"] = collect(root, ["/"], sizes)

    winner = None
    for size in sizes.values():
        if unused + size >= needed:
            if winner is None or size < winner:
                winner = size

    return winner

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
