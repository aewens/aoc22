from pprint import pprint

add = lambda a, b: a + b
mul = lambda a, b: a * b
class Monkey:
    def __init__(self, items, op, value, test, if_true, if_false):
        self.items = items
        self.op = op
        self.value = value
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

        self.p2 = None
        self.count = 0
        self.debug = False

    def catch(self, item):
        self.items.append(item)

    def inspect(self):
        self.count = self.count + 1

        item = self.items[0]
        self.items = self.items[1:]

        value = item if self.value == "old" else self.value
        worry = self.op(item, value)
        if self.p2 is None:
            worry = worry // 3

        else:
            worry = worry % self.p2

        #if self.debug:
        #    print(item, self.op(item, value), worry)

        return worry

    def turn(self):
        remap = list()
        while len(self.items) > 0:
            worry = self.inspect()
            if worry % self.test == 0:
                remap.append((self.if_true, worry))
                continue

            remap.append((self.if_false, worry))

        return remap

    def __repr__(self):
        items = ", ".join(str(item) for item in self.items)
        return f"Monkey({items})"

def parse(puzzle_input, p2=False):
    monkeys = dict()
    index = None
    items = list()
    op = None
    value = None
    test = None
    if_true = None
    if_false = None

    mod = 1
    for line in puzzle_input:
        line = line.strip()
        if len(line) == 0:
            continue

        if line.startswith("Monkey"):
            index = int(line.split(" ", 1)[1][:-1])

        if line.startswith("Starting"):
            starting = line.split(": ", 1)[1]
            for item in starting.split(", "):
                items.append(int(item))

        if line.startswith("Operation"):
            *ignore, sign, value = line.split()
            op = add if sign == "+" else mul
            if value != "old":
                value = int(value)

        if line.startswith("Test"):
            test = int(line.split()[-1])
            mod = mod * test

        if line.startswith("If true"):
            if_true = int(line.split()[-1])

        if line.startswith("If false"):
            if_false = int(line.split()[-1])

            monkey = Monkey(items, op, value, test, if_true, if_false)
            monkeys[index] = monkey

            index = None
            items = list()
            op = None
            test = None
            if_true = None
            if_false = None

    if p2:
        for monkey in monkeys.values():
            monkey.p2 = mod

    return monkeys

def run(puzzle_input, p2=False):
    rounds = 10000 if p2 else 20
    monkeys = parse(puzzle_input, p2)
    assert len(monkeys) > 0, monkeys
    for i in range(rounds):
        for m in range(len(monkeys)):
            monkey = monkeys[m]
            #if m == 0:
            #    monkey.debug = i == 0
            remap = monkey.turn()
            for (index, item) in remap:
                monkeys[index].catch(item)
                #if i == 0:
                #    print(m, index, item)

        #for m in range(len(monkeys)):
        #    monkey = monkeys[m]
        #    if i == 0:
        #        print(m, monkey.items)

    counts = sorted(monkey.count for monkey in monkeys.values())
    #print(counts)
    return counts[-1] * counts[-2]

def p1(puzzle_input):
    return run(puzzle_input)

def p2(puzzle_input):
    # NOTE - SLOW, but works
    #return run(puzzle_input, True)
    return None

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
