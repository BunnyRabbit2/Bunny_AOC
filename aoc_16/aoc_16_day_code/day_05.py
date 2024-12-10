"""Code to solve puzzle for day 05"""
import os
from hashlib import md5

def solve():
    """Solves the day"""
    file_loc = "inputs/day05.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC16_INPUT_DAY05':
            print("Invalid input file header: Day05")
            return ''
     
        return input_file.read()
    else:
        print("Day 05 input file does not exist")
        return ''

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 05 Puzzle 1 - NO INPUTS")
    else:
        room_id = inputs

        passcode = ''

        current_index = 1

        while (len(passcode) < 8):
            check_hash = md5(f'{room_id}{current_index}'.encode())

            check_hash = check_hash.hexdigest()

            if check_hash[:5] == '00000':
                passcode += check_hash[5]
            current_index += 1
        
        output = passcode

        print("Day 05 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 05 Puzzle 2 - NO INPUTS")
    else:
        room_id = inputs

        passcode = {}

        current_index = 1

        while (len(passcode) < 8):
            check_hash = md5(f'{room_id}{current_index}'.encode())

            check_hash = check_hash.hexdigest()

            if check_hash[:5] == '00000':
                pos = check_hash[5]

                if pos.isdigit():
                    pos = int(pos)
                    if pos not in passcode and 0 <= pos <= 7:
                        passcode[pos] = check_hash[6]

            current_index += 1

        output = ''.join([passcode[i] for i in range(8)])

        print("Day 05 Puzzle 2 Solution - " + str(output))
    