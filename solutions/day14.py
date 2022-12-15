from utils import slow
from pprint import pprint
#from time import sleep

def build(puzzle_input):
    rocks = dict()
    cutoff = None
    for line in puzzle_input:
        #print("LINE", line)
        start = None
        paths = line.split(" -> ")
        for path in paths:
            #print("PATH", path)
            pair = path.split(",", 1)
            x = int(pair[0])
            y = int(pair[1])
            rocks[(x, y)] = True
            if cutoff is None or y > cutoff:
                cutoff = y

            if start is None:
                start = x, y
                continue

            sx, sy = start

            ry = range(1)
            if y > sy:
                ry = range(1, y-sy+1)

            elif y < sy:
                ry = range(-1, y-sy-1, -1)

            rx = range(1)
            if x > sx:
                rx = range(1, x-sx+1)

            elif x < sx:
                rx = range(-1, x-sx-1, -1)

            for j in ry:
                for i in rx:
                    #print(sx+i, sy+j)
                    rocks[(sx+i, sy+j)] = True

            start = x, y

    return rocks, cutoff

def fall(sx, sy, sand, rocks, cutoff, p2=False):
    nx, ny = sx, sy+1
    if p2 and ny == cutoff + 2:
        return False, (sx, sy)

    if not p2 and ny > cutoff:
        return None, (sx, sy)

    check = nx, ny
    if True not in [rocks.get(check), sand.get(check)]:
        return True, check

    nx = sx-1
    check = nx, ny
    if True not in [rocks.get(check), sand.get(check)]:
        return True, check

    nx = sx+1
    check = nx, ny
    if True not in [rocks.get(check), sand.get(check)]:
        return True, check

    return False, (sx, sy)

def pour(source, rocks, cutoff, p2=False):
    sand = dict()
    sx, sy = source
    while True:
        falling, (sx, sy) = fall(sx, sy, sand, rocks, cutoff, p2=p2)
        if falling is None:
            return sand

        if not falling:
            sand[(sx, sy)] = True
            if (sx, sy) == source:
                return sand

            sx, sy = source
            continue

def p1(puzzle_input):
    source = 500, 0
    sand = pour(source, *build(puzzle_input))
    return len(sand)

def p2(puzzle_input):
    source = 500, 0
    sand = pour(source, *build(puzzle_input), p2=True)
    return len(sand)

@slow
def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
