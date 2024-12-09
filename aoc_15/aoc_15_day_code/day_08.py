"""Code to solve puzzle for day 08"""
import os
from re import escape


def solve():
    """Solves the day"""
    file_loc = "inputs/day08.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY08':
            print("Invalid input file header: Day08")
            return ''

        return input_file.read()
    else:
        print("Day 08 input file does not exist")
        return ''


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 08 Puzzle 1 - NO INPUTS")
    else:
        lines = inputs.split('\n')

        char_count = 0
        mem_count = 0

        for l in lines:
            char_count += len(l)
            mem_count += len(eval(l))

        output = char_count - mem_count

        print("Day 08 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 08 Puzzle 2 - NO INPUTS")
    else:
        lines = inputs.split('\n')

        char_count = 0
        new_char_count = 0

        for l in lines:
            char_count += len(l)

            el = l.replace('\\', '\\\\').replace('"', '\\"')
            new_char_count += len(el) + 2

        output = new_char_count - char_count

        print("Day 08 Puzzle 2 Solution - " + str(output))
