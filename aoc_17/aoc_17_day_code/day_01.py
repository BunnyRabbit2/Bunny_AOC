"""Code to solve puzzle for day 01"""
import os

def solve():
    """Solves the day"""
    file_loc = "inputs/day01.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC17_INPUT_DAY01':
            print("Invalid input file header: Day01")
            return ''
     
        return input_file.read()
    else:
        print("Day 01 input file does not exist")
        return ''

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 01 Puzzle 1 - NO INPUTS")
    else:
        output = 0

        print("Day 01 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 01 Puzzle 2 - NO INPUTS")
    else:
        output = 0

        print("Day 01 Puzzle 2 Solution - " + str(output))
    