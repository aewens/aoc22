from pprint import pprint
from time import sleep
from sys import exit

def build(puzzle_input):
    actions = list()
    line = puzzle_input[0]
    for char in line:
        if char == "<":
            actions.append(-1)

        elif char == ">":
            actions.append(1)

    return actions

def place(grid, rock):
    for y, row in rock.items():
        for x, col in row.items():
            grid[y][x] = 1

    c = max(grid.keys())
    f = min(grid.keys())
    for y in range(c-1, f-1, -1):
        if 1 in grid[y]:
            #print(y+1)
            return y+1

def down(grid, rock, f):
    moved = dict()
    for y, row in rock.items():
        for x, col in row.items():
            if y-1 < f or grid[y-1][x] != 0:
                return False, place(grid, rock)

        moved[y-1] = row

    return True, moved

def left(grid, rock):
    moved = dict()
    for y, row in rock.items():
        moved[y] = dict()
        for x, col in row.items():
            if grid[y][x-1] != 0:
                return False, rock

            moved[y][x-1] = col

    return True, moved

def right(grid, rock):
    moved = dict()
    for y, row in rock.items():
        moved[y] = dict()
        for x, col in row.items():
            if grid[y][x+1] != 0:
                return False, rock

            moved[y][x+1] = col

    return True, moved

def top(grid, w, c, f):
    state = [0] * (w+1)
    for x in range(w+1):
        o = 0
        y = c-1
        while True:
            if y < f:
                break

            if grid[y][x] == 1:
                state[x] = o
                break

            o = o + 1
            y = y - 1

    return state

def assign(bi, ai, h, hs, dhs):
    key = bi, ai
    hs[key] = h

    pai = ai - 1
    if ai == 0:
        pai = steps - 1

    ph = hs.get((bi, pai))
    if ph is not None:
        d = h - ph
        dh = dhs.get(key, list())
        if d in dh:
            print(bi, ai, d)

        else:
            dh.append(h-ph)

        dhs[key] = dh

def run(actions, amount, p2=False):
    cache = actions[:]
    rocks = [
        (1, [(0,0),(0,1),(0,2),(0,3)]),
        (3 ,[(0,1),(1,0),(1,1),(1,2),(2,1)]),
        (3, [(2,2),(1,2),(0,0),(0,1),(0,2)]),
        (4, [(0,0),(1,0),(2,0),(3,0)]),
        (2, [(0,0),(0,1),(1,0),(1,1)])
    ]
    count = len(rocks)
    steps = len(actions)
    print(count * steps)

    h = 0
    w = 6
    grid = dict()
    for y in range(3):
        grid[y] = [0] * (w+1)

    ai = -1
    hs = dict()
    dhs = dict()
    last = dict()
    replay = None
    store = None
    for r in range(amount):
        if replay is not None:
            break

        remove = None
        c = max(grid.keys())
        f = min(grid.keys())
        for y in range(c-1, f-1, -1):
            if sum(grid[y]) == w+1:
                remove = y
                break

        if remove is not None:
            for y in range(f, remove):
                grid.pop(y)

            f = remove

        bi = r % count
        size, block = rocks[bi]
        resize = (h+3+size) - (c-1)
        if resize > 0:
            for i in range(resize):
                grid[c] = [0] * (w+1)
                c = c + 1

        oy, ox = h+3, 2
        xmin = None
        xmax = None
        rock = dict()
        for (by, bx) in block:
            y = by+oy
            x = bx+ox

            if xmin is None or x < xmin:
                xmin = x

            if xmax is None or x > xmax:
                xmax = x

            row = rock.get(y)
            if row is None:
                row = dict()
                rock[y] = row

            row[x] = True

        while True:
            ai = (ai + 1) % steps
            action = actions[ai]
            if (action == -1 and xmin == 0) or (action == 1 and xmax == w):
                moved, result = down(grid, rock, f)
                if not moved:
                    ph = h
                    h = result
                    #assign(bi, ai, h, hs, dhs)
                    state = top(grid, w, c, f)
                    if sum(state) % (w+1) == 0:
                        lst = last.get((bi, ai))
                        if lst is not None:
                            store = r - lst[0], h-lst[1]
                            replay = bi, ai
                            break

                        last[(bi, ai)] = r, h

                    key = bi, ai, *state
                    prev = hs.get(key)
                    if prev is not None:
                        pprev = dhs.get(key)
                        dhs[key] = h-prev

                    hs[key] = h
                    break

                rock = result
                continue

            if action == -1:
                moved, result = left(grid, rock)
                if moved:
                    xmin = xmin - 1
                    xmax = xmax - 1

                moved, result = down(grid, result, f)
                if not moved:
                    h = result
                    #assign(bi, ai, h, hs, dhs)
                    state = top(grid, w, c, f)
                    if sum(state) % (w+1) == 0:
                        lst = last.get((bi, ai))
                        if lst is not None:
                            store = r - lst[0], h-lst[1]
                            replay = bi, ai
                            break

                        last[(bi, ai)] = r, h

                    key = bi, ai, *state
                    prev = hs.get(key)
                    if prev is not None:
                        pprev = dhs.get(key)
                        dhs[key] = h-prev

                    hs[key] = h
                    break

                rock = result
                continue

            if action == 1:
                moved, result = right(grid, rock)
                if moved:
                    xmin = xmin + 1
                    xmax = xmax + 1

                moved, result = down(grid, result, f)
                if not moved:
                    h = result
                    #assign(bi, ai, h, hs, dhs)
                    state = top(grid, w, c, f)
                    if sum(state) % (w+1) == 0:
                        lst = last.get((bi, ai))
                        if lst is not None:
                            store = r - lst[0], h-lst[1]
                            replay = bi, ai
                            break

                        last[(bi, ai)] = r, h

                    key = bi, ai, *state
                    prev = hs.get(key)
                    if prev is not None:
                        pprev = dhs.get(key)
                        dhs[key] = h-prev

                    hs[key] = h
                    break

                rock = result
                continue

    if p2:
        print(store)
        magic = store[0]
        loops, rem = divmod(amount, magic)
        skip = loops * store[1]
        return skip, rem

    return h

def p1(puzzle_input):
    actions = build(puzzle_input)
    return run(actions, 2022)

def p2(puzzle_input):
    amount = 1000000000000
    actions = build(puzzle_input)
    fst, lst = run(actions, amount, True)
    result = fst + run(actions, lst)
    return result

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
