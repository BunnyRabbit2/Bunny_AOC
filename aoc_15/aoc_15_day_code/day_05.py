"""Code to solve puzzle for day 05"""
import os

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
        if not first_line == 'AOC15_INPUT_DAY05':
            print("Invalid input file header: Day05")
            return ''
     
        return input_file.read()
    else:
        print("Day 05 input file does not exist")
        return ''

def check_string_is_nice(test_string):
    """Checks if a string is nice for puzzle 1"""
    has_pair = False
    naughty_pairs = ["ab","cd","pq","xy"]
    vowels = []
    vowelCheck = ["a","e","i","o","u"]

    for i in range(len(test_string)):
        pair_check = test_string[i:i+2]
        if pair_check in naughty_pairs:
            return False

        if len(pair_check) > 1:
            if pair_check[0] == pair_check[1]:
                has_pair = True

        char = test_string[1]

        if char in vowelCheck:
            vowels.append(char)

    if has_pair and len(vowels) >= 3:
        return True
    else:
        return False

def check_string_is_nice_alt(test_string):
    """Checks if a string is nice for puzzle 2"""
    has_repeat_pair = False
    has_triple_set = False

    for i in range(len(test_string)):
        test_pair = test_string[i:i+2]
        if len(test_pair) > 1:
            new_test_string = test_string
            new_test_string = new_test_string[:i] + "--" + new_test_string[i + 2:]

            for j in range(len(test_string)):
                newTestPair = new_test_string[j:j+2]
                if newTestPair == test_pair:
                    has_repeat_pair = True
            
        check_triple = test_string[i:i+3]
        if len(check_triple) > 2:
            if check_triple[0] == check_triple[2] and check_triple[0] != check_triple[1]:
                has_triple_set = True

    if has_triple_set and has_repeat_pair:
        return True
    else:
        return False

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 05 Puzzle 1 - NO INPUTS")
    else:
        inputs = inputs.split()
        output = 0

        for i in inputs:
            if check_string_is_nice(i):
                output += 1

        print("Day 05 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 05 Puzzle 2 - NO INPUTS")
    else:
        inputs = inputs.split()
        output = 0

        for i in inputs:
            if check_string_is_nice_alt(i):
                output += 1

        print("Day 05 Puzzle 2 Solution - " + str(output))
    