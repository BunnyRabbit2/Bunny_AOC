import os
import json

def solve():
    file_loc = "inputs/day12.json"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return json.loads(file.read())
    else:
        print("Day 12 input file does not exist")

def countHook(obj):
    return obj

def get_count(json):
    if type(json) in [str]:
        return 0
    if type(json) in [int,float]:
        return json
    if type(json) is list:
        return sum(map(get_count,json))
    if type(json) is dict:
        return sum(map(get_count,json.items()))
    if type(json) is tuple:
        return sum(map(get_count,json))

def get_count_no_red(json):
    if type(json) in [str]:
        return 0
    if type(json) in [int,float]:
        return json
    if type(json) is list:
        return sum(map(get_count_no_red,json))
    if type(json) is dict:
        if "red" in json.values():
            return 0
        return sum(map(get_count_no_red,json.items()))
    if type(json) is tuple:
        return sum(map(get_count_no_red,json))

def solve_puzzle_1(file_location):
    json_file = load_inputs(file_location)

    output = get_count(json_file)

    print(f'Day 12 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location):
    json_file = load_inputs(file_location)

    output = get_count_no_red(json_file)

    print(f'Day 12 Puzzle 2 Solution - {output}')