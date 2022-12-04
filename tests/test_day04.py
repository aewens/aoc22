from .context import get_puzzle, solutions, obtain

index = 4
INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""[1:-1].split("\n")

def test_d4():
    puzzle = [line.strip() for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle)
    assert s1 == 2, "p1 is wrong"

    p2 = script("p2")
    s2 = p2(puzzle)
    assert s2 == 4, "p2 is wrong"
