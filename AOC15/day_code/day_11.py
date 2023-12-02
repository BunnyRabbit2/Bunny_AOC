import os
import re


def solve():
    file_loc = "inputs/day11.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read()
    else:
        print("Day 11 input file does not exist")


def increment_string(s):
    r = list(s)[::-1]
    i = 0
    for c in r:
        if c == 'z':
            r[i] = 'a'
        else:
            r[i] = chr(ord(c)+1)
            break
        i += 1

    return ''.join(r[::-1])


def check_password(s):
    if 'i' in s or 'o' in s or 'l' in s:
        return False

    has_straight = False

    for i in range(len(s)-2):
        if ord(s[i]) == ord(s[i+1]) - 1 and ord(s[i]) == ord(s[i+2]) - 2:
            has_straight = True

    if not has_straight:
        return False

    re_c = re.findall(r'(.)\1', s)
    if len(re_c) < 2:
        return False

    return True


def get_next_password(s):
    valid = False

    while not valid:
        s = increment_string(s)
        valid = check_password(s)

    return s


def solve_puzzle_1(file_location):
    input = load_inputs(file_location)

    output = get_next_password(input)

    print(f'Day 11 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    input = load_inputs(file_location)

    output = get_next_password(input)
    output = get_next_password(output)

    print(f'Day 11 Puzzle 2 Solution - {output}')
