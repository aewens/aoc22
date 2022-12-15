#!/usr/bin/env python3

from utils import noop, get_puzzle, get_solutions

from time import perf_counter
from argparse import ArgumentParser, FileType
from sys import exit

parser = ArgumentParser()
parser.add_argument("-d", "--day", dest="day")
parser.add_argument("-s", "--skip", dest="skip", action="append")
parser.add_argument("-S", "--slow", dest="slow", action="store_true")
parser.add_argument("-o", "--override", dest="override", type=FileType("r"))

def maybe_int(value):
    return value if value is None else int(value)

def handle_result(day, result):
    if result is None:
        print(day, "ERROR")
        return

    a, b = result
    print(f"{day}a", a)
    print(f"{day}b", b)

def main():
    args = parser.parse_args()

    divider = "-" * 80
    print("AOC 2022 Solutions:")
    print(divider)
    solutions = get_solutions()

    index = maybe_int(args.day)
    if index is not None:
        start = perf_counter()

        day = f"Day {index:02}"
        puzzle = get_puzzle(index)
        if args.override is not None:
            puzzle = args.override.read().strip().split("\n")

        solution = solutions[index]
        handle_result(day, solution(puzzle))
        print(f"~ {perf_counter()-start:.05f}s")
        print(divider)
        exit(0)

    #for index, solution in get_solutions().items():
    skips = list()
    if args.skip is not None:
        skips = [maybe_int(s) for s in args.skip]

    for index in range(len(solutions)):
        if index in skips:
            continue

        solution = solutions.get(index)
        if solution is None:
            continue

        if not args.slow and getattr(solution, "slow", None):
            continue

        start = perf_counter()
        day = f"Day {index:02}"
        puzzle = get_puzzle(index)
        handle_result(day, solution(puzzle))
        print(f"~ {perf_counter()-start:.05f}s")
        print(divider)

if __name__ == "__main__":
    main()
