from .context import get_puzzle, solutions, obtain

index = 12
INPUT = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""[1:-1].split("\n")

def test_d12():
    puzzle = [line for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle)
    assert s1 == 31, f"p1 is wrong: {s1}"

    p2 = script("p2")
    s2 = p2(puzzle)
    assert s2 == 29, f"p2 is wrong: {s2}"
