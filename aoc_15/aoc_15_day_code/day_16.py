"""Code to solve puzzle for day 16"""
import os


def solve():
    """Solves the day"""
    file_loc = "inputs/day16.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY16':
            print("Invalid input file header: Day16")
            return ''

        return input_file.read()
    else:
        print("Day 16 input file does not exist")
        return ''


def create_sues(inputs):
    """Turns the input into a list of sues. Sue 0 is the check sue"""
    sue_list = []

    for line in inputs:
        new_sue = {
            "children": 0,
            "cats": 0,
            "samoyeds": 0,
            "pomeranians": 0,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 0,
            "trees": 0,
            "cars": 0,
            "perfumes": 0
        }

        sue_input = [s.split(': ') for s in line.split(': ', 1)[1].split(', ')]

        for s in sue_input:
            new_sue[s[0]] = int(s[1])

        sue_list.append(new_sue)

    return sue_list


def find_best_sue(sue_list, alt_check=False):
    """Finds the best matching sue to the check sue. Can use an alternate checking method"""
    check_sue = sue_list[0]

    sue_list = sue_list[1:]

    best_match_count = 0
    best_sue = 0

    for i, sue in enumerate(sue_list):
        match_count = 0

        for k in sue:
            if alt_check:
                if k in ["cats", "trees"] and sue[k] > check_sue[k]:
                    match_count += 1
                elif k in ["pomeranians", "goldfish"] and sue[k] < check_sue[k]:
                    match_count += 1
                elif sue[k] == check_sue[k]:
                    match_count += 1
            else:
                if sue[k] == check_sue[k]:
                    match_count += 1

        if match_count > best_match_count:
            best_match_count = match_count
            best_sue = i + 1

    return best_sue


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 16 Puzzle 1 - NO INPUTS")
    else:
        sue_list = create_sues(inputs.split('\n'))

        output = find_best_sue(sue_list)

        print("Day 16 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 16 Puzzle 2 - NO INPUTS")
    else:
        sue_list = create_sues(inputs.split('\n'))

        output = find_best_sue(sue_list, alt_check=True)

        print("Day 16 Puzzle 2 Solution - " + str(output))
