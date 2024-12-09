"""Code to solve puzzle for day 12"""
import os
import json


def solve():
    """Solves the day"""
    file_loc = "inputs/day12.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY12':
            print("Invalid input file header: Day12")
            return ''

        return input_file.read()
    else:
        print("Day 12 input file does not exist")
        return ''


def get_count(json_file):
    """Counts all numbers in a given JSON file"""
    if type(json_file) in [str]:
        return 0
    if type(json_file) in [int, float]:
        return json_file
    if type(json_file) is list:
        return sum(map(get_count, json_file))
    if type(json_file) is dict:
        return sum(map(get_count, iter(json_file.items())))
    if type(json_file) is tuple:
        return sum(map(get_count, json_file))


def get_count_no_red(json_file):
    """Counts all nubers in a given JSON file apart from those that are labelled as 'red'"""
    if type(json_file) in [str]:
        return 0
    if type(json_file) in [int, float]:
        return json_file
    if type(json_file) is list:
        return sum(map(get_count_no_red, json_file))
    if type(json_file) is dict:
        if "red" in json_file.values():
            return 0
        return sum(map(get_count_no_red, iter(json_file.items())))
    if type(json_file) is tuple:
        return sum(map(get_count_no_red, json_file))


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 12 Puzzle 1 - NO INPUTS")
    else:
        output = get_count(json.loads(inputs))

        print("Day 12 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 12 Puzzle 2 - NO INPUTS")
    else:
        output = get_count_no_red(json.loads(inputs))

        print("Day 12 Puzzle 2 Solution - " + str(output))
