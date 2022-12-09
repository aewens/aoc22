from pprint import pprint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def where(self):
        return self.x, self.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Rope:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def resolve(self):
        dx = abs(self.head.x - self.tail.x)
        dy = abs(self.head.y - self.tail.y)

        ox = -1 if self.head.x > self.tail.x else 1
        oy = -1 if self.head.y > self.tail.y else 1

        if dx > 1:
            self.tail.x = self.head.x + ox
            if dy > 0:
                self.tail.y = self.tail.y - oy

            return

        if dy > 1:
            self.tail.y = self.head.y + oy
            if dx > 0:
                self.tail.x = self.tail.x - ox

            return

    def left(self):
        self.head.x = self.head.x-1

    def right(self):
        self.head.x = self.head.x+1

    def up(self):
        self.head.y = self.head.y-1

    def down(self):
        self.head.y = self.head.y+1

    def __repr__(self):
        return f"{self.head} | {self.tail}"

def p1(puzzle_input):
    rope = Rope(Point(0, 0), Point(0, 0))

    seen = dict()
    seen[rope.tail.where()] = True
    for line in puzzle_input:
        letter, number = line.split(" ")
        for i in range(int(number)):
            if letter == "R":
                rope.right()

            if letter == "L":
                rope.left()

            if letter == "U":
                rope.up()

            if letter == "D":
                rope.down()

            rope.resolve()
            seen[rope.tail.where()] = True

    return len(seen)

def p2(puzzle_input):
    head = Rope(Point(0, 0), Point(0, 0))
    prev = None
    ropes = list()
    for i in range(9):
        prev = head if prev is None else ropes[-1]
        rope = Rope(prev.tail, Point(0, 0))
        ropes.append(rope)

    tail = ropes[-1].head

    seen = dict()
    seen[tail.where()] = True
    for line in puzzle_input:
        letter, number = line.split(" ")
        #print(line)
        for i in range(int(number)):
            if letter == "R":
                head.right()

            if letter == "L":
                head.left()

            if letter == "U":
                head.up()

            if letter == "D":
                head.down()

            head.resolve()
            for rope in ropes:
                rope.resolve()

            seen[tail.where()] = True
            #print(i, 0, head)
            #for r, rope in enumerate(ropes):
            #    print(i, r+1, rope)

        #print(line)
        #print(0, head)
        #for r, rope in enumerate(ropes):
        #    print(r+1, rope)

    return len(seen)

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
