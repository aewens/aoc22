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

def p1(puzzle_input):
    flows, tunnels = build(puzzle_input)
    result = step("AA", flows, tunnels)
    return result

def p2(puzzle_input):
    return None

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
