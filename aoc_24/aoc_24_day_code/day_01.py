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
        if not first_line == 'AOC24_INPUT_DAY01':
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
        line_pairs = []
        for l in inputs.split('\n'):
            l_nums = l.split()
            line_pairs.append((int(l_nums[0]), int(l_nums[1])))

        left_list, right_list = zip(*line_pairs)

        sorted_pairs = zip(sorted(left_list), sorted(right_list))

        output = sum([abs(p[0] - p[1]) for p in sorted_pairs])

        print("Day 01 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 01 Puzzle 2 - NO INPUTS")
    else:
        line_pairs = []
        for l in inputs.split('\n'):
            l_nums = l.split()
            line_pairs.append((int(l_nums[0]), int(l_nums[1])))

        left_list, right_list = zip(*line_pairs)

        occurences = {n: right_list.count(n) for n in left_list}

        output = sum([n * occurences[n] for n in left_list])

        print("Day 01 Puzzle 2 Solution - " + str(output))
    