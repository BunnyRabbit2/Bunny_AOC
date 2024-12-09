"""Code to solve puzzle for day 09"""
import os
from itertools import permutations


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
        if not first_line == 'AOC15_INPUT_DAY09':
            print("Invalid input file header: Day09")
            return ''

        return input_file.read()
    else:
        print("Day 09 input file does not exist")
        return ''


def find_distances(loc_inputs):
    """Finds the shortest and longest routes for a given set of cities"""
    places = set()
    distances = {}

    for s in loc_inputs:
        (source, _, dest, _, distance) = s.split()
        places.add(source)
        places.add(dest)
        distances.setdefault(source, {})[dest] = int(distance)
        distances.setdefault(dest, {})[source] = int(distance)

    shortest = -1
    longest = 0

    for items in permutations(places):
        dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
        if shortest == -1:
            shortest = dist
        shortest = min(shortest, dist)
        longest = max(longest, dist)

    return (shortest, longest)


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 09 Puzzle 1 - NO INPUTS")
    else:
        output = find_distances(inputs.split('\n'))

        print("Day 09 Puzzle 1 Solution - " + str(output[0]))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 09 Puzzle 2 - NO INPUTS")
    else:
        output = find_distances(inputs.split('\n'))

        print("Day 09 Puzzle 2 Solution - " + str(output[1]))
