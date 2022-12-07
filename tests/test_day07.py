from .context import get_puzzle, solutions, obtain

index = 7
INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""[1:-1].split("\n")

def test_d7():
    puzzle = [line for line in INPUT]
    script = obtain(index)

    p1 = script("p1")
    s1 = p1(puzzle)

    assert s1 == 95437, f"p1 is wrong: {s1}"

    p2 = script("p2")
    s2 = p2(puzzle)
    assert s2 == 24933642, f"p2 is wrong: {s2}"
