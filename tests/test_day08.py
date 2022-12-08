from .context import get_puzzle, solutions, obtain

index = 8
INPUT = """
30373
25512
65332
33549
35390
"""[1:-1].split("\n")

def test_d8():
    puzzle = [line for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle)

    assert s1 == 21, f"p1 is wrong: {s1}"

    p2 = script("p2")
    s2 = p2(puzzle)
    assert s2 == 8, f"p2 is wrong: {s2}"

