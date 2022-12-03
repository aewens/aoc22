def p1(puzzle_input):
    remap = dict()
    remap[True] = lambda x: ord(x) - 96
    remap[False] = lambda x: ord(x) - 38

    common = list()
    for line in puzzle_input:
        compartments = dict()
        compartments[0] = dict()
        compartments[1] = dict()

        cutoff = len(line) // 2
        count = 0
        index = 0
        found = False
        for item in line:
            compartments[index][item] = True
            if not found and index == 1:
                if compartments[0].get(item):
                    priority = remap[item.islower()](item)
                    common.append(priority)
                    found = True

            count = count + 1
            if count == cutoff:
                index = 1


    return sum(common)

def p2(puzzle_input):
    remap = dict()
    remap[True] = lambda x: ord(x) - 96
    remap[False] = lambda x: ord(x) - 38

    group = 0
    bag = 0
    prev = None
    curr = dict()
    badges = list()
    for line in puzzle_input:
        compartments = dict()
        compartments[0] = dict()
        compartments[1] = dict()

        for item in line:
            if prev is None:
                curr[item] = True
                continue

            if prev.get(item):
                curr[item] = True

        prev = curr
        curr = dict()
        bag = bag + 1
        if bag == 3:
            for item in prev:
                priority = remap[item.islower()](item)
                badges.append(priority)

            prev = None
            group = group + 1
            bag = 0

    return sum(badges)

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
