from pprint import pprint

def build(puzzle_input):
    sensors = dict()
    beacons = dict()
    distances = dict()
    for line in puzzle_input:
        s_line, b_line = line.split(": ", 1)

        srx, sry = s_line[10:].split(", ", 1)
        sx = int(srx[2:])
        sy = int(sry[2:])
        sensor = sx, sy
        sensors[sensor] = True

        brx, bry = b_line[21:].split(", ", 1)
        bx = int(brx[2:])
        by = int(bry[2:])
        beacon = bx, by
        beacons[beacon] = True

        distances[sensor] = abs(sx-bx) + abs(sy-by)

    return sensors, beacons, distances

def coverage(y, sensors, beacons, distances):
    covered = dict()
    for (sx, sy), distance in distances.items():
        dy = abs(sy-y)
        if dy > distance:
            continue

        covered[(sx, y)] = True
        dx = distance - dy
        if dx == 0:
            continue

        for o in range(1, dx+1):
            covered[(sx-o, y)] = True
            covered[(sx+o, y)] = True

    for beacon in beacons.keys():
        covered.pop(beacon, None)

    return covered

def p1(puzzle_input, y=2000000):
    # NOTE - SLOW, but works
    #if y > 10:
    #    return None

    return len(coverage(y, *build(puzzle_input)))

def p2(puzzle_input, cap=4000000):
    return None

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
