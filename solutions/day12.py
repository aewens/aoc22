from pprint import pprint
from heapq import heappop, heappush

infinity = float("inf")

def parse(puzzle_input):
    x, y = 0, 0
    p2 = list()
    start = None
    end = None
    hmap = dict()

    for line in puzzle_input:
        for char in line:
            elevation = None
            if char == "S":
                start = x, y
                elevation = 0

            elif char == "E":
                end = x, y
                elevation = 25

            else:
                elevation = ord(char) - ord("a")

            if elevation == 0:
                p2.append((x, y))

            hmap[(x, y)] = elevation
            x = x + 1

        y = y + 1
        x = 0

    return hmap, start, end, p2

def get_routes(hmap, width, height):
    routes = dict()
    for y in range(height):
        for x in range(width):
            elevation = hmap.get((x, y))
            if elevation is None:
                continue

            routes[(x, y)] = list()
            neighbors = [
                (x-1, y),
                (x+1, y),
                (x, y-1),
                (x, y+1)
            ]

            for neighbor in neighbors:
                n_elevation = hmap.get(neighbor)
                if n_elevation is None:
                    continue

                diff = n_elevation - elevation
                if diff > 1:
                    continue

                routes[(x, y)].append(neighbor)

    return routes

def dijkstra(routes, start, end):
    seen = dict()
    points = [(0, start)]
    distances = {start: 0}

    while len(points) > 0:
        distance, point = heappop(points)
        if point == end:
            return distance

        if seen.get(point) is not None:
            continue

        seen[point] = True
        neighbors = routes[point]
        for neighbor in neighbors:
            route = distance + 1
            dist = distances.get(neighbor)
            if dist is None or route < dist:
                distances[neighbor] = route
                heappush(points, (route, neighbor))

    return infinity

def p1(puzzle_input):
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    hmap, start, end, _ = parse(puzzle_input)
    routes = get_routes(hmap, width, height)
    return dijkstra(routes, start, end)

def p2(puzzle_input):
    # NOTE - SLOW, but works
    return None

    width = len(puzzle_input[0])
    height = len(puzzle_input)
    hmap, _, end, starts = parse(puzzle_input)
    routes = get_routes(hmap, width, height)

    winner = None
    for start in starts:
        steps = dijkstra(routes, start, end)
        if winner is None or steps < winner:
            winner = steps

    return winner

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
