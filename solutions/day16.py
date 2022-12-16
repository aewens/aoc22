from pprint import pprint
from time import sleep

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

def step(pointer, valves, flows, tunnels, prev=None, clock=30, pressure=0):
    if clock < 2:
        return pressure

    remain = [k for k, v in flows.items() if v > 0 and not valves[k]]
    if len(remain) == 0:
        return pressure

    routes = tunnels[pointer]

    skip = None
    if len(routes) > 1 and prev and prev in routes:
        skip = prev

    winner = 0
    static = flows, tunnels, pointer
    for route in routes:
        if route == skip:
            continue

        opened = valves[route]
        flow = flows[route]
        result = None
        display = None
        if flow == 0 or opened:
            suffix = *static, clock-1, pressure
            result = step(route, valves, *suffix)

        else:
            altered = {**valves}
            altered[route] = True

            change = (clock-2) * flow
            suffix = *static, clock-2, pressure+change
            left = step(route, altered, *suffix)

            suffix = *static, clock-1, pressure
            right = step(route, valves, *suffix)

            result = left if left > right else right

        if result is None:
            continue

        if result > winner:
            winner = result

    return winner

def p1(puzzle_input):
    flows, tunnels = build(puzzle_input)
    valves = {k: False for k in flows.keys()}
    result = step("AA", valves, flows, tunnels)

def p2(puzzle_input):
    return None

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
