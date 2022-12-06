def find_start(puzzle_input, size):
    line = puzzle_input[0]
    prev = list(line[:size-1])
    count = size - 1
    for char in line[size-1:]:
        prev.append(char)
        count = count + 1
        if len(set(prev)) == size:
            return count
            break

        prev = prev[1:]
        continue

def p1(puzzle_input):
    return find_start(puzzle_input, 4)

def p2(puzzle_input):
    return find_start(puzzle_input, 14)

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
