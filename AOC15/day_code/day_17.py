import os
import itertools


def solve():
    file_loc = "inputs/day17.txt"
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
        print("Day 17 input file does not exist")


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    output = 0

    for i in range(len(inputs)):
        sub = 0
        for comb in itertools.combinations(inputs, i):
            if sum(comb) == 150:
                sub += 1
        output += sub

    print(f'Day 17 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    output = 0
    min_containers = 0

    for i in range(len(inputs)):
        sub = 0
        for comb in itertools.combinations(inputs, i):
            if sum(comb) == 150:
                min_containers = i
                sub += 1
        output += sub
        if min_containers > 0:
            break

    print(f'Day 17 Puzzle 2 Solution - {output}')
