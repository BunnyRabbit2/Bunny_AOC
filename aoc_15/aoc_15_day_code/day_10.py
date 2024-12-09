"""Code to solve puzzle for day 10"""
import os
import re


def solve():
    """Solves the day"""
    file_loc = "inputs/day10.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY10':
            print("Invalid input file header: Day10")
            return ''

        return input_file.read()
    else:
        print("Day 10 input file does not exist")
        return ''


def look_and_say(input_string):
    """Returns a string with look-and-say applied to it"""
    re_d = re.compile(r'((\d)\2*)')

    def replace(match_obj):
        input_string = match_obj.group(1)
        return str(len(input_string)) + input_string[0]

    return re_d.sub(replace, input_string)


def loop_look_and_say(loop_count, input_string):
    for i in range(loop_count):
        input_string = look_and_say(input_string)

    return input_string


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 10 Puzzle 1 - NO INPUTS")
    else:
        output = len(loop_look_and_say(40, inputs))

        print("Day 10 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 10 Puzzle 2 - NO INPUTS")
    else:
        output = len(loop_look_and_say(50, inputs))

        print("Day 10 Puzzle 2 Solution - " + str(output))
