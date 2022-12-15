from .context import get_puzzle, solutions, obtain

index = 15
INPUT = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""[1:-1].split("\n")

def test_d15():
    puzzle = [line for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle, 10)
    assert s1 == 26, f"p1 is wrong: {s1}"

    p2 = script("p2")
    s2 = p2(puzzle, 20)
    assert s2 == 56000011, f"p2 is wrong: {s2}"
