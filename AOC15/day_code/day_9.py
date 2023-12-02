import os
from itertools import permutations


def solve():
    file_loc = "inputs/day9.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.readlines()
    else:
        print("Day 9 input file does not exist")


def findDistances(inputs):
    places = set()
    distances = {}

    for s in inputs:
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
    inputs = load_inputs(file_location)

    output = findDistances(inputs)

    print(f'Day 9 Puzzle 1 Solution - {output[0]}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    output = findDistances(inputs)

    print(f'Day 9 Puzzle 1 Solution - {output[1]}')
