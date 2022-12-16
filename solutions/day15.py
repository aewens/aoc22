from utils import slow
from pprint import pprint
from collections import namedtuple

Range = namedtuple("Range", ["min", "max"])

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

        dx = abs(sx-bx)
        dy = abs(sy-by)
        distances[sensor] = dx + dy

    return sensors, beacons, distances

def merge(spans):
    while True:
        seen = dict()
        merged = list()
        changed = False
        for i in range(len(spans)):
            for j in range(len(spans)):
                if i == j:
                    continue

                span = spans[i]
                other = spans[j]
                if seen.get(other):
                    continue

                seen[other] = True
                if span.min == other.min and span.max == other.max:
                    merged.append(span)
                    continue

                if span.min <= other.min and span.max >= other.min:
                    changed = True
                    combine = Range(span.min, max(span.max, other.max))
                    seen[combine] = True
                    merged.append(combine)
                    continue

                if span.min <= other.max and span.max >= other.max:
                    changed = True
                    combine = Range(min(span.min, other.min), span.max)
                    seen[combine] = True
                    merged.append(combine)
                    continue

                merged.append(other)

        if len(merged) == 0:
            return spans

        if not changed:
            return merged

        spans = merged
        continue

def coverage(y, sensors, beacons, distances):
    search = list()
    for (sx, sy), distance in distances.items():
        dy = abs(sy-y)
        if dy > distance:
            continue

        dx = distance - dy
        span = Range(sx-dx, sx+dx)
        if len(search) == 0:
            search.append(span)
            continue

        remove = list()
        replaced = False
        for i in range(len(search)):
            check = search[i]
            if span.min < check.min and span.max < check.min:
                continue

            if span.min > check.max and span.max > check.max:
                continue

            if span.min < check.min and span.max > check.max:
                remove.append(check)
                continue

            replaced = True
            if span.min >= check.min and span.max <= check.max:
                continue

            if span.min < check.min and span.max >= check.min:
                search[i] = Range(span.min, max(span.max, check.max))
                continue

            if span.min <= check.max and span.max > check.max:
                search[i] = Range(min(span.min, check.min), span.max)
                continue

        for entry in remove:
            search.remove(entry)

        if not replaced:
            search.append(span)

    search = merge(search)

    offset = 0
    for (sx, sy) in sensors.keys():
        if sy != y:
            continue

        for check in search:
            if sx >= check.min and sx <= check.max:
                offset = offset + 1

    for (bx, by) in beacons.keys():
        if by != y:
            continue

        for check in search:
            if bx >= check.min and bx <= check.max:
                offset = offset + 1

    total = -offset
    for check in search:
        total = total + (check.max-check.min+1)

    return total

def frequency(cap, sensors, beacons, distances):
    for y in range(cap, 0, -1):
        if cap > 20 and y % 100000 == 0:
            print(f"{100*(1-y/cap):.02f}%")

        cache = list()
        search = list()
        for (sx, sy), distance in distances.items():
            dy = abs(sy-y)
            if dy > distance:
                continue

            dx = distance - dy
            span = Range(sx-dx, sx+dx)
            if span.max < 0 or span.min > cap:
                continue

            span = Range(max(0, span.min), min(cap, span.max))
            cache.append(span)
            if len(search) == 0:
                search.append(span)
                continue

            remove = list()
            replaced = False
            for i in range(len(search)):
                check = search[i]
                if span.min < check.min and span.max < check.min:
                    continue

                if span.min > check.max and span.max > check.max:
                    continue

                if span.min < check.min and span.max > check.max:
                    remove.append(check)
                    continue

                replaced = True
                if span.min >= check.min and span.max <= check.max:
                    continue

                if span.min < check.min and span.max >= check.min:
                    search[i] = Range(span.min, max(span.max, check.max))
                    continue

                if span.min <= check.max and span.max > check.max:
                    search[i] = Range(min(span.min, check.min), span.max)
                    continue

            for entry in remove:
                search.remove(entry)

            if not replaced:
                search.append(span)

        merged = merge(search)
        if len(merged) == 1 and merged[0].min == 0 and merged[0].max == cap:
            continue

        if len(merged) == 1:
            return None

        total = 0
        for span in merged:
            total = total + span.max - span.min

        if total == cap:
            continue

        if total != cap-1:
            for span in merged:
                if span.min == 0:
                    x = span.max + 1
                    return x * 4000000 + y

def border(x, y, distance):
    for dx in range(distance + 2):
        dy = distance + 1 - dx
        yield x - dx, y - dy
        yield x - dx, y + dy
        yield x + dx, y - dy
        yield x + dx, y + dy

def freq(cap, distances):
    for (sx, sy), distance in distances.items():
        for x, y in border(sx, sy, distance):
            if x < 0 or x > cap:
                continue

            if y < 0 or y > cap:
                continue

            skip = False
            for (ox, oy), dist in distances.items():
                if abs(x-ox) + abs(y-oy) > dist:
                    continue

                skip = True
                break

            if not skip:
                return x * 4000000 + y

def p1(puzzle_input, y=2000000):
    return coverage(y, *build(puzzle_input))

def p2(puzzle_input, cap=4000000):
    # NOTE - SSSLLLOOOWWW, but works
    # NOTE - Original solution
    #return frequency(cap, *build(puzzle_input))

    # NOTE - Slightly faster learned from community
    return freq(cap, build(puzzle_input)[-1])

@slow
def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
