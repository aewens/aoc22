def p1(puzzle_input):
    inventory = dict()
    index = 0
    inventory[index] = 0

    most = None
    elf = None
    for line in puzzle_input:
        if len(line) == 0:
            total = inventory[index]
            if most is None or total > most:
                most = total
                elf = index

            index = index + 1
            inventory[index] = 0
            continue

        inventory[index] = inventory[index] + int(line)

    total = inventory[index]
    if most is None or total > most:
        most = total
        elf = index

    return most, inventory

def p2(inventory):
    invert = {v: k for k, v in inventory.items()}
    keys = reversed(sorted(invert.keys()))
    total = 0
    count = 0
    for key in keys:
        if count >= 3:
            break

        total = total + key
        count = count + 1

    return total

def solve(puzzle_input):
    most, inventory = p1(puzzle_input)
    return most, p2(inventory)

