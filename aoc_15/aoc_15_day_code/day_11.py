"""Code to solve puzzle for day 11"""
import os
import re


def solve():
    """Solves the day"""
    file_loc = "inputs/day11.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY11':
            print("Invalid input file header: Day11")
            return ''

        return input_file.read()
    else:
        print("Day 11 input file does not exist")
        return ''


def increment_string(input_string):
    """Increments a string as though it were a base 26 number"""
    reverse_string = list(input_string)[::-1]
    for i, char in enumerate(reverse_string):
        if char == 'z':
            reverse_string[i] = 'a'
        else:
            reverse_string[i] = chr(ord(char)+1)
            break

    return ''.join(reverse_string[::-1])


def check_password(input_string):
    """Checks if a password is valid"""
    if 'i' in input_string or 'o' in input_string or 'l' in input_string:
        return False

    has_straight = False

    for i in range(len(input_string)-2):
        if ord(input_string[i]) == ord(input_string[i+1]) - 1 and ord(input_string[i]) == ord(input_string[i+2]) - 2:
            has_straight = True

    if not has_straight:
        return False

    rC = re.findall(r'(.)\1', input_string)
    if len(rC) < 2:
        return False

    return True


def get_next_password(input_string):
    """Gets the next valid password given an input password"""
    valid = False

    while not valid:
        input_string = increment_string(input_string)
        valid = check_password(input_string)

    return input_string


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 11 Puzzle 1 - NO INPUTS")
    else:
        output = get_next_password(inputs)

        print("Day 11 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 11 Puzzle 2 - NO INPUTS")
    else:
        output = get_next_password(inputs)
        output = get_next_password(output)

        print("Day 11 Puzzle 2 Solution - " + str(output))
