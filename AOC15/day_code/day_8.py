import os
import re


def solve():
    file_loc = "inputs/day8.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split()
    else:
        print("Day 8 input file does not exist")


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    char_count = 0
    mem_count = 0

    for s in inputs:
        char_count += len(s)
        mem_count += len(eval(s))

    output = char_count - mem_count

    print(f'Day 8 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    char_count = 0
    new_char_count = 0

    for s in inputs:
        char_count += len(s)
        new_char_count += len(re.escape(s)) + 2

    output = new_char_count - char_count

    print(f'Day 8 Puzzle 2 Solution - {output}')
