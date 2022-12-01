from .context import get_puzzle, solutions, obtain

index = 1
INPUT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""[1:-1].split("\n")

def test_d1p1():
    script = obtain(index)
    p1 = script("p1")
    puzzle = [line.strip() for line in INPUT]
    most, inventory = p1(puzzle)
    assert most == 24000, "p1 is wrong"

    p2 = script("p2")
    assert p2(inventory) == 45000, "p2 is wrong"
