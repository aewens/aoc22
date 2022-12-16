from .context import get_puzzle, solutions, obtain

index = 16
INPUT = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""[1:-1].split("\n")

def test_d16():
    puzzle = [line for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle)
    # NOTE - Works, but SLOW!!
    #assert s1 == 1651, f"p1 is wrong: {s1}"

    #p2 = script("p2")
    #s2 = p2(puzzle)
    #assert s2 == 56000011, f"p2 is wrong: {s2}"
