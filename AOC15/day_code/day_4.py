import os
from hashlib import md5


def solve():
    file_loc = "inputs/day4.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read()
    else:
        print("Day 4 input file does not exist")


def find_advent_coin(secret, check_string):
    has_found_coin = False
    current_num = 0

    while not has_found_coin:
        encoded_string = f'{secret}{current_num}'.encode("utf-8")
        test_hash = md5(encoded_string).hexdigest()
        if test_hash[0:len(check_string)] == check_string:
            has_found_coin = True
        else:
            current_num += 1

    return current_num


def solve_puzzle_1(file_location):
    input = load_inputs(file_location)

    output = find_advent_coin(input, "00000")

    print(f'Day 4 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    input = load_inputs(file_location)

    output = find_advent_coin(input, "000000")

    print(f'Day 4 Puzzle 2 Solution - {output}')
