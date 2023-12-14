import os
from itertools import pairwise

def solve():
    file_loc = "inputs/day09.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC23_INPUT_DAY09':
            print("Invalid input file header: Day09")
            return False
     
        return file.read()
    else:
        print("Day 09 input file does not exist")

def gen_diff_lists(input_lines):
    reading_lists = [[int(v) for v in l.split()] for l in input_lines]

    diff_lists = [[] for i in range(len(reading_lists))]

    for i, l in enumerate(reading_lists):
        working_list = l
        diff_lists[i].append(l)
        while True:
            d_list = [y-x for (x,y) in pairwise(working_list)]
            diff_lists[i].append(d_list)
            working_list = d_list[::]
            zero_check = [d == 0 for d in d_list]
            if False not in zero_check:
                break

    return diff_lists

def create_predicted_value(diff_list: list[list]):
    diff_list = diff_list[::-1]
    diff_list[0].insert(0, 0)
    diff_list[0].append(0)

    for x, l in enumerate(diff_list):
        if x == len(diff_list) - 1: break
        diff_list[x + 1].append(l[-1] + diff_list[x + 1][-1])
        diff_list[x + 1].insert(0, diff_list[x + 1][0] - l[0])
    
    return (diff_list[-1][0], diff_list[-1][-1])

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return
    
    test_inputs = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

    diff_lists = gen_diff_lists(inputs.splitlines())

    predicted_values = []
    for l in diff_lists:
        val = create_predicted_value(l)[1]
        predicted_values.append(val)

    output = sum(predicted_values)

    print(f'Day 09 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    diff_lists = gen_diff_lists(inputs.splitlines())

    predicted_values = []
    for l in diff_lists:
        val = create_predicted_value(l)[0]
        predicted_values.append(val)

    output = sum(predicted_values)

    print(f'Day_09 Puzzle 2 Solution - {output}')
    