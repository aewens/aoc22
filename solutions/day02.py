def p1(puzzle_input):
    shape = dict()
    shape["X"] = 1
    shape["Y"] = 2
    shape["Z"] = 3

    outcome = dict()
    outcome["A"] = dict()
    outcome["A"]["X"] = 3
    outcome["A"]["Y"] = 6
    outcome["A"]["Z"] = 0
    outcome["B"] = dict()
    outcome["B"]["X"] = 0
    outcome["B"]["Y"] = 3
    outcome["B"]["Z"] = 6
    outcome["C"] = dict()
    outcome["C"]["X"] = 6
    outcome["C"]["Y"] = 0
    outcome["C"]["Z"] = 3

    total = 0
    for line in puzzle_input:
        fst, snd = line.split(" ", 1)
        total = total + shape[snd] + outcome[fst][snd]

    return total

def p2(puzzle_input):
    shape = dict()
    shape["X"] = 0
    shape["Y"] = 3
    shape["Z"] = 6

    outcome = dict()
    outcome["A"] = dict()
    outcome["A"]["X"] = 3
    outcome["A"]["Y"] = 1
    outcome["A"]["Z"] = 2
    outcome["B"] = dict()
    outcome["B"]["X"] = 1
    outcome["B"]["Y"] = 2
    outcome["B"]["Z"] = 3
    outcome["C"] = dict()
    outcome["C"]["X"] = 2
    outcome["C"]["Y"] = 3
    outcome["C"]["Z"] = 1

    total = 0
    for line in puzzle_input:
        fst, snd = line.split(" ", 1)
        total = total + shape[snd] + outcome[fst][snd]

    return total

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)

