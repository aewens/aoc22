def p1(puzzle_input):
    count = 0
    for line in puzzle_input:
        knowns = list()
        for pair in line.split(",", 1):
            pa, pb = pair.split("-", 1)
            knowns.append(set(range(int(pa), int(pb)+1)))

        overlap = knowns[0].intersection(knowns[1])
        if len(overlap) == min(len(knowns[0]), len(knowns[1])):
            count = count + 1

    return count

def p2(puzzle_input):
    count = 0
    for line in puzzle_input:
        knowns = list()
        for pair in line.split(",", 1):
            pa, pb = pair.split("-", 1)
            knowns.append(set(range(int(pa), int(pb)+1)))

        overlap = knowns[0].intersection(knowns[1])
        if len(overlap) > 0:
            count = count + 1

    return count

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
