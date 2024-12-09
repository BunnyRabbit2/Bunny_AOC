"""Code to solve puzzle for day 04"""
import os
from hashlib import md5

def solve():
    """Solves the day"""
    file_loc = "inputs/day04.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY04':
            print("Invalid input file header: Day04")
            return ''
     
        return input_file.read()
    else:
        print("Day 04 input file does not exist")
        return ''

def find_advent_coin(secret, check_string):
    """Calculates an advent coin for a given secret"""
    found_coin = False
    current_number = 0

    while not found_coin:
        test_hash = md5(f'{secret}{current_number}'.encode()).hexdigest()
        if test_hash[0:len(check_string)] == check_string:
            found_coin = True
        else:
            current_number += 1

    return current_number

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 04 Puzzle 1 - NO INPUTS")
    else:
        output = find_advent_coin(inputs, "00000")

        print("Day 04 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 04 Puzzle 2 - NO INPUTS")
    else:
        output = find_advent_coin(inputs, "000000")

        print("Day 04 Puzzle 2 Solution - " + str(output))
    