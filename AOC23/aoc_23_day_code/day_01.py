import os
import re


def solve():
    file_loc = "inputs/day01.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC23_INPUT_DAY01':
            print("Invalid input file header: Day01")
            return False

        return file.read()
    else:
        print("Day 01 input file does not exist")


def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    file_lines = inputs.split('\n')

    number_search = re.compile(r'(\d{1})')

    line_digits = []

    for line in file_lines:
        digit_search_res = number_search.findall(line)
        line_digits.append(int(digit_search_res[0] + digit_search_res[-1]))

    output = sum(line_digits)

    print("Day 01 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    file_lines = inputs.split('\n')

    number_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    number_search_fwd = re.compile(
        r'(\d{1}|' + '|'.join([n for n in number_dict]) + ')')
    number_search_rev = re.compile(
        r'(\d{1}|' + '|'.join([n[::-1] for n in number_dict]) + ')')

    line_digits = []

    for line in file_lines:
        first_digit = number_search_fwd.findall(line)[0]
        first_digit = number_dict.get(first_digit, first_digit)

        last_digit = number_search_rev.findall(line[::-1])[0][::-1]
        last_digit = number_dict.get(last_digit, last_digit)

        line_digits.append(int(first_digit + last_digit))

    output = sum(line_digits)

    print("Day 01 Puzzle 2 Solution - " + str(output))
