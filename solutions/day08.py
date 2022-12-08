def build(puzzle_input):
    grid = dict()
    for j, line in enumerate(puzzle_input):
        grid[j] = dict()
        for i, tree in enumerate(line):
            grid[j][i] = int(tree)

    return grid

def up(grid, y, x):
    focus = grid[y][x]
    for j in range(y):
        if focus <= grid[j][x]:
            return False

    return True

def down(grid, y, x):
    focus = grid[y][x]
    height = len(grid)
    for j in range(height-1, y, -1):
        if focus <= grid[j][x]:
            return False

    return True

def left(grid, y, x):
    focus = grid[y][x]
    for i in range(x):
        if focus <= grid[y][i]:
            return False

    return True

def right(grid, y, x):
    focus = grid[y][x]
    width = len(grid[y])
    for i in range(width-1, x, -1):
        if focus <= grid[y][i]:
            return False

    return True

def score(grid, y, x):
    width = len(grid[y])
    height = len(grid)

    focus = grid[y][x]

    us = 0
    for j in range(1, y+1):
        us = us + 1
        if grid[y-j][x] >= focus:
            break

    ds = 0
    for j in range(1, height-y):
        ds = ds + 1
        if grid[y+j][x] >= focus:
            break

    ls = 0
    for i in range(1, x+1):
        ls = ls + 1
        if grid[y][x-i] >= focus:
            break

    rs = 0
    for i in range(1, width-x):
        rs = rs + 1
        if grid[y][x+i] >= focus:
            break

    return us * ds * ls * rs

def p1(puzzle_input):
    width = len(puzzle_input[0])
    height = len(puzzle_input)

    grid = build(puzzle_input)

    givens = 2 * width + 2 * height - 4
    visible = 0
    for y in range(1, height-1):
        for x in range(1, width-1):
            if up(grid, y, x):
                visible = visible + 1
                continue

            if down(grid, y, x):
                visible = visible + 1
                continue

            if left(grid, y, x):
                visible = visible + 1
                continue

            if right(grid, y, x):
                visible = visible + 1
                continue

    return givens + visible

def p2(puzzle_input):
    width = len(puzzle_input[0])
    height = len(puzzle_input)

    grid = build(puzzle_input)
    winner = None

    for y in range(1, height-1):
        for x in range(1, width-1):
            scored = score(grid, y, x)
            if winner is None or scored > winner:
                winner = scored

    return winner

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)

