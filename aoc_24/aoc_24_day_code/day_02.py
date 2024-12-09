"""Code to solve puzzle for day 02"""
import os
from itertools import pairwise, combinations

def solve():
    """Solves the day"""
    file_loc = "inputs/day02.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC24_INPUT_DAY02':
            print("Invalid input file header: Day02")
            return ''
     
        return input_file.read()
    else:
        print("Day 02 input file does not exist")
        return ''
    
def is_report_safe(report_nums) -> bool:
    """Returns is the report handed in is safe
    
    Uses the following rules:
        1. The numbers must always increase or always decrease
        2. The difference cannot be 0 or larger than three
    """
    diffs = [p[0] - p[1] for p in pairwise(report_nums)]

    if 0 in diffs:
        return False
    
    if any([n > 3 or n < -3 for n in diffs]):
        return False
    
    return all([n > 0 for n in diffs]) or all([n < 0 for n in diffs])

def is_report_safe_dampened(report_nums) -> bool:
    """Returns is the report handed in is safe when problems are dampened
    
    Will check each report and then the reports that fail are checked with each single entry removed
    """
    if is_report_safe(report_nums):
        return True
    
    possible_indexes = [i for i in range(len(report_nums))]

    possible_combis = combinations(possible_indexes, len(possible_indexes) - 1)

    for combi in possible_combis:
        if is_report_safe([report_nums[i] for i in combi]):
            return True

    return False

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 02 Puzzle 1 - NO INPUTS")
    else:
        report_list = [[int(n) for n in l.split()] for l in inputs.split('\n')]

        output = sum([1 if is_report_safe(r) else 0 for r in report_list])

        print("Day 02 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 02 Puzzle 2 - NO INPUTS")
    else:
        report_list = [[int(n) for n in l.split()] for l in inputs.split('\n')]

        output = sum([1 if is_report_safe_dampened(r) else 0 for r in report_list])

        print("Day 02 Puzzle 2 Solution - " + str(output))
    