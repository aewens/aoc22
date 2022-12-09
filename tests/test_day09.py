from .context import get_puzzle, solutions, obtain

index = 9
INPUT = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""[1:-1].split("\n")

OTHER = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""[1:-1].split("\n")

def test_d9():
    puzzle = [line for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle)

    assert s1 == 13, f"p1 is wrong: {s1}"

    p2 = script("p2")

    s2 = p2(puzzle)
    assert s2 == 1, f"p2 is wrong: {s2}"

    puzzle = [line for line in OTHER]
    s2 = p2(puzzle)
    assert s2 == 36, f"p2 is wrong: {s2}"
