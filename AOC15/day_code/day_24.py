import os
from itertools import combinations
from operator import mul
import functools


def solve():
    file_loc = "inputs/day24.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        lines = file.readlines()
        n = []
        for l in lines:
            n.append(int(l))
        return n
    else:
        print("Day 24 input file does not exist")


def has_weight(packages, sub, weight, parts):
    for i in range(1, len(packages)):
        for s in (c for c in combinations(packages, i) if sum(c) == weight):
            if sub == 2:
                return True
            elif sub < parts:
                return has_weight(list(set(packages) - set(s)), sub-1, weight, parts)
            elif has_weight(list(set(packages) - set(s)), sub-1, weight, parts):
                return functools.reduce(mul, s, 1)


def solve_puzzle_1(file_location):
    packages = load_inputs(file_location)

    parts = 3
    output = has_weight(packages, parts, sum(packages) // parts, parts)

    print(f'Day 24 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    packages = load_inputs(file_location)

    parts = 4
    output = has_weight(packages, parts, sum(packages) // parts, parts)

    print(f'Day 24 Puzzle 2 Solution - {output}')
