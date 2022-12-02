from .context import get_puzzle, solutions, obtain

index = 2
INPUT = """
A Y
B X
C Z
"""[1:-1].split("\n")

def test_d2():
    puzzle = [line.strip() for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle)
    assert s1 == 15, "p1 is wrong"

    p2 = script("p2")
    s2 = p2(puzzle)
    assert s2 == 12, "p2 is wrong"
