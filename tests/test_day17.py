from .context import get_puzzle, solutions, obtain

index = 17
INPUT = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""[1:-1].split("\n")

def test_d17():
    puzzle = [line for line in INPUT]
    script = obtain(index)

    #p1 = script("p1")
    #s1 = p1(puzzle)
    #assert s1 == 3068, f"p1 is wrong: {s1}"

    p2 = script("p2")
    s2 = p2(puzzle)
    assert s2 == 1514285714288, f"p2 is wrong: {s2}"
