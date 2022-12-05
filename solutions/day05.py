from utils import get_puzzle

def move(puzzle_input, part2=False):
    mode = 0
    columns = dict()
    for line in puzzle_input:
        if mode == 0:
            if len(line.strip()) == 0:
                mode = 1
                continue

            row = 1
            while len(line) > 0:
                crate, line = line[:3], line[3:]
                if len(line) > 0:
                    line = line[1:]

                if crate[0] == " " and crate[1] != " ":
                    break

                if columns.get(row) is None:
                    columns[row] = list()

                name = crate[1]
                if name == " ":
                    row = row + 1
                    continue

                columns[row].append(name)
                row = row + 1

            continue

        if len(line) == 0:
            continue

        line = line[5:]
        count, line = line.split(" from ", 1)
        count = int(count)
        src, dest = line.split(" to ")
        src = int(src)
        dest = int(dest)

        s_column = columns[src]
        d_column = columns[dest]
        if not part2:
            for i in range(count):
                crate, s_column = s_column[0], s_column[1:]
                d_column = [crate] + d_column

        else:
            crates, s_column = s_column[:count], s_column[count:]
            d_column = crates + d_column

        columns[src] = s_column
        columns[dest] = d_column

    final = ""
    for column, crates in columns.items():
        final = final + crates[0]

    return final

def p1(puzzle_input):
    return move(puzzle_input)

def p2(puzzle_input):
    return move(puzzle_input, True)

def solve(ignore):
    puzzle_input = get_puzzle(5, nostrip=True)
    return p1(puzzle_input), p2(puzzle_input)

