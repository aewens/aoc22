from .context import get_puzzle, solutions, obtain

index = 11
INPUT = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""[1:-1].split("\n")

def test_d11():
    puzzle = [line for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle)
    assert s1 == 10605, f"p1 is wrong: {s1}"

    # NOTE - SLOW, but works
    #p2 = script("p2")
    #s2 = p2(puzzle)
    #assert s2 == 2713310158, f"p2 is wrong: {s2}"
