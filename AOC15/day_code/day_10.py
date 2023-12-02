import os
import re


def solve():
    file_loc = "inputs/day10.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read()
    else:
        print("Day 10 input file does not exist")


def look_and_say(s):
    re_d = re.compile(r'((\d)\2*)')

    def replace(match_obj):
        s = match_obj.group(1)
        return str(len(s)) + s[0]

    return re_d.sub(replace, s)


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    for i in range(40):
        inputs = look_and_say(inputs)

    output = len(inputs)

    print(f'Day 10 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    for i in range(50):
        inputs = look_and_say(inputs)

    output = len(inputs)

    print(f'Day 10 Puzzle 2 Solution - {output}')
