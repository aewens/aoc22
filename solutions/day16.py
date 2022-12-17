from pprint import pprint
from time import sleep
from heapq import heappush, heappop

def build(puzzle_input):
    flows = dict()
    tunnels = dict()
    for line in puzzle_input:
        fst, snd = line.split("; ")
        _, raw = snd.split("valve", 1)
        routes = raw.split(", ")
        routes[0] = routes[0][1:]
        if routes[0].startswith(" "):
            routes[0] = routes[0][1:]

        head, tail = fst.split(" has ", 1)
        valve = head[6:]
        flow = int(tail[10:])

        flows[valve] = flow
        tunnels[valve] = routes

    return flows, tunnels

def resolve(pointer, targets, tunnels):
    seen = dict()
    seen[pointer] = True

    options = dict()

    points = [([], pointer)]
    while len(points) > 0:
        path, valve = heappop(points)
        for tunnel in tunnels[valve]:
            route = [*path, valve]
            size = len(route)

            if targets.get(tunnel):
                routes = options[tunnel] = options.get(tunnel, list())
                count = len(routes)
                cap = None if count == 0 else len(routes[0])

                if cap is not None and size < cap:
                    for r in range(count):
                        if len(routes[r]) > size:
                            routes.pop(r)

                if cap is None or size <= cap:
                    routes.append(route)

            if seen.get(tunnel):
                continue

            seen[tunnel] = True
            heappush(points, (route, tunnel))

    return options

def step(
    pointer,
    flows,
    tunnels,
    opened=None,
    clock=30,
    pressure=0
):
    if clock < 2:
        return pressure

    if opened is None:
        opened = {k: False for k in flows.keys()}

    targets = {k: v for k, v in flows.items() if v > 0 and not opened[k]}
    if len(targets) == 0:
        return pressure

    winner = 0
    static = flows, tunnels

    options = resolve(pointer, targets, tunnels)
    #print(pointer, clock, pressure, len(targets))
    #pprint(options)
    for valve, routes in options.items():
        flow = flows[valve]
        for route in routes:
            ticks = len(route)+1
            result = pressure
            if ticks <= clock:
                altered = {**opened}
                altered[valve] = True

                change = (clock-ticks) * flow
                suffix = *static, altered, clock-ticks, pressure+change
                result = step(valve, *suffix)

            if result > winner:
                winner = result

    return winner

def step2(
    pointers,
    flows,
    tunnels,
    opened=None,
    clocks=[26, 26],
    pressure=0
):
    if max(clocks) < 2:
        return pressure

    if clocks[1] > clocks[0]:
        clocks[0], clocks[1] = clocks[1], clocks[0]
        pointers[0], pointers[1] = pointers[1], pointers[0]

    if opened is None:
        opened = {k: False for k in flows.keys()}

    targets = {k: v for k, v in flows.items() if v > 0 and not opened[k]}
    if len(targets) == 0:
        return pressure

    winner = 0
    static = flows, tunnels

    options1 = dict()
    if clocks[0] > 2:
        options1 = resolve(pointers[0], targets, tunnels)

    options2 = dict()
    if clocks[1] > 2:
        options2 = resolve(pointers[1], targets, tunnels)

    #print(pointer, clock, pressure, len(targets))
    #pprint(options1)
    #pprint(options2)
    for valve1, routes1 in options1.items():
        flow1 = flows[valve1]
        for valve2, routes2 in options2.items():
            flow2 = flows[valve2]
            if valve1 == valve2:
                continue

            altered = {**opened}
            altered[valve1] = True
            altered[valve2] = True

            for route1 in routes1:
                ticks1 = len(route1)+1
                for route2 in routes2:
                    ticks2 = len(route2)+1

                    result = pressure
                    change = 0
                    timers = clocks[:]
                    if ticks1 <= clocks[0]:
                        timers[0] = clocks[0]-ticks1
                        change = change + timers[0] * flow1

                    if ticks2 <= clocks[1]:
                        timers[1] = clocks[1]-ticks2
                        change = change + timers[1] * flow2

                    if change > 0:
                        suffix = *static, altered, timers, pressure+change
                        result = step2([valve1, valve2], *suffix)

                    if result > winner:
                        winner = result

    return winner

def p1(puzzle_input):
    flows, tunnels = build(puzzle_input)
    return step("AA", flows, tunnels)

def p2(puzzle_input):
    flows, tunnels = build(puzzle_input)
    return step2(["AA", "AA"], flows, tunnels)

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
