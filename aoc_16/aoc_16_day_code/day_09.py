"""Code to solve puzzle for day 09"""
import os
import re

def solve():
    """Solves the day"""
    file_loc = "inputs/day09.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC16_INPUT_DAY09':
            print("Invalid input file header: Day09")
            return ''
     
        return input_file.read()
    else:
        print("Day 09 input file does not exist")
        return ''
    
def decode_string(encoded_str):
    decoded_string = ''

    step = 0
    while step < len(encoded_str):
        step_amount = 1

        next_char = encoded_str[step]

        if next_char == '(':
            command = ''

            command_step = 1
            command_char = encoded_str[step + command_step]

            while command_char != ')':
                command += command_char
                command_step += 1
                command_char = encoded_str[step + command_step]

            r, m = [int(v) for v in command.split('x')]

            copy_step = step + command_step + 1

            copy_slice = encoded_str[copy_step:copy_step + r]

            decoded_string += ''.join([copy_slice for c in range(m)])

            step_amount = len(command) + 2 + r
        else:
            decoded_string += next_char
        
        step += step_amount

    return decoded_string

def get_decoded_string_len(encoded_str):
    if '(' in encoded_str and encoded_str[0] != '(':
        c = '('

    decoded_len = 0

    command_search = re.compile(r'\(\d*x\d*\)')

    next_command = command_search.search(encoded_str)

    if next_command is not None:
        next_command = next_command.group()

        command_len = len(next_command)

        r, m = [int(v) for v in re.sub('\(|\)', '', next_command).split('x')]

        m_string = encoded_str[command_len:command_len + r]

        decoded_len += (r * m)

        decoded_len += get_decoded_string_len(m_string)

        decoded_len += get_decoded_string_len(encoded_str[command_len + r:])

    return decoded_len

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 09 Puzzle 1 - NO INPUTS")
    else:
        # output = len(decode_string(inputs))

        output = get_decoded_string_len(inputs)

        print("Day 09 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 09 Puzzle 2 - NO INPUTS")
    else:
        output = 0

        print("Day 09 Puzzle 2 Solution - " + str(output))
    