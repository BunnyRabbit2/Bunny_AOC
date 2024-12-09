"""Code to solve puzzle for day 25"""
import os
import re

def solve():
    """Solves the day"""
    file_loc = "inputs/day25.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY25':
            print("Invalid input file header: Day25")
            return ''
     
        return input_file.read()
    else:
        print("Day 25 input file does not exist")
        return ''

def generate_code_field(width,height):
    x,y = 0,0
    value = 20151125
    grid = []

    for y in range(height):
        grid.append([])
        for x in range(width):
            grid[y].append(0)

    def next_i(i):
        return i + 1
    def next_n(n):
        return (n * 252533) % 33554393

    for y in range(height):
        for i in range(y+1):
            yi,xi = y-i,i
            grid[yi][xi] = value
            value = next_n(value)

    return grid

def get_value_from_grid(x,y):
    total = x+y
    grid = generate_code_field(total,total)
    return grid[y-1][x-1]

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 25 Puzzle 1 - NO INPUTS")
    else:
        nums = [int(s) for s in re.findall(r'\b\d+\b', inputs)]

        output = get_value_from_grid(nums[1],nums[0])

        print(f'Day 25 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location):
    # inputs = load_inputs(file_location)

    output = 0

    print(f'Day 25 Puzzle 2 Solution - {output}')