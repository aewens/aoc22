from .context import get_puzzle, solutions, obtain

index = 3
INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""[1:-1].split("\n")

def test_d3():
    puzzle = [line.strip() for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle)
    assert s1 == 157, "p1 is wrong"

    p2 = script("p2")
    s2 = p2(puzzle)
    assert s2 == 70, "p2 is wrong"

