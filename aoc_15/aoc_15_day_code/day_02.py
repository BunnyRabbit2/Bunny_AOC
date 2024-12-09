"""Code to solve puzzle for day 02"""
import os

def solve():
    """Solves the day"""
    file_loc = "inputs/day02.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY02':
            print("Invalid input file header: Day02")
            return ''

        return input_file.read()
    else:
        print("Day 02 input file does not exist")
        return ''

def calculate_wrapping(l, w, h):
    """Calculates the wrapping needed for a present of the given size"""
    side_1 = l*w
    side_2 = l*h
    side_3 = w*h

    smallest_side = min(side_1, side_2, side_3)

    surface_area = side_1 * 2 + side_2 * 2 + side_3 * 2

    return surface_area + smallest_side

def calculate_ribbon(l, w, h):
    """Calculate the ribbon needed for a present of the given size"""
    per_1 = l*2 + w*2
    per_2 = l*2 + h*2
    per_3 = w*2 + h*2

    ribbon = min(per_1, per_2, per_3)
    bow = l*w*h

    return ribbon + bow

def get_lwh_from_string(lwh_string):
    """Returns the length, width and height from input string"""
    values = lwh_string.split('x')
    return (int(values[0]), int(values[1]), int(values[2]))

def calculate_total_sf(inputs):
    """Calculates the total suqare footage of the wrapping and feet of ribbon required for presents given"""
    total_wrapping_sf = 0
    total_ribbon_f = 0

    for i in inputs:
        values = get_lwh_from_string(i)
        total_wrapping_sf += calculate_wrapping(values[0], values[1], values[2])
        total_ribbon_f += calculate_ribbon(values[0], values[1], values[2])

    return (total_wrapping_sf, total_ribbon_f)

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 02 Puzzle 1 - NO INPUTS")
    else:
        output = calculate_total_sf(inputs.split())

        print("Day 02 Puzzle 1 Solution - " + str(output[0]))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 02 Puzzle 2 - NO INPUTS")
    else:
        output = calculate_total_sf(inputs.split())

        print("Day 02 Puzzle 2 Solution - " + str(output[1]))
