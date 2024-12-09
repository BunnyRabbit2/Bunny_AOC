"""Code to solve puzzle for day 24"""
import os
from itertools import combinations
from operator import mul
import functools

def solve():
    """Solves the day"""
    file_loc = "inputs/day24.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY24':
            print("Invalid input file header: Day24")
            return ''
     
        return input_file.read()
    else:
        print("Day 24 input file does not exist")
        return ''

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 24 Puzzle 1 - NO INPUTS")
    else:
        output = 0

        print("Day 24 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 24 Puzzle 2 - NO INPUTS")
    else:
        output = 0

        print("Day 24 Puzzle 2 Solution - " + str(output))

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
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 24 Puzzle 1 - NO INPUTS")
    else:
        weights = [int(w) for w in inputs.split('\n')]
        
        parts = 3
        output = has_weight(weights, parts, sum(weights) // parts, parts)

        print(f'Day 24 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 24 Puzzle 2 - NO INPUTS")
    else:
        weights = [int(w) for w in inputs.split('\n')]

        parts = 4
        output = has_weight(weights, parts, sum(weights) // parts, parts)

        print(f'Day 24 Puzzle 2 Solution - {output}')
    