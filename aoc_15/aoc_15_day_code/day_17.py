"""Code to solve puzzle for day 17"""
import os
from itertools import combinations


def solve():
    """Solves the day"""
    file_loc = "inputs/day17.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY17':
            print("Invalid input file header: Day17")
            return ''

        return input_file.read()
    else:
        print("Day 17 input file does not exist")
        return ''


def find_possible_combis(container_list):
    """Finds the possible ways to make 150L with the tubs given"""
    combination_number = 0

    for i in range(len(container_list)):
        for combination in combinations(container_list, i):
            if sum(combination) == 150:
                combination_number += 1

    return combination_number


def find_possible_combis_for_min_tubs(container_list):
    """Finds the possible ways to make 150L with the minimum tubs out of the tubs given"""
    minimum_tubs = 0

    for i in range(len(container_list)):
        combination_number = 0
        for combination in combinations(container_list, i):
            if sum(combination) == 150:
                combination_number += 1
                minimum_tubs = i

        if minimum_tubs != 0:
            break

    return combination_number


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 17 Puzzle 1 - NO INPUTS")
    else:
        container_list = [int(l) for l in inputs.split('\n')]

        output = find_possible_combis(container_list)

        print("Day 17 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 17 Puzzle 2 - NO INPUTS")
    else:
        container_list = [int(l) for l in inputs.split('\n')]

        output = find_possible_combis_for_min_tubs(container_list)

        print("Day 17 Puzzle 2 Solution - " + str(output))
