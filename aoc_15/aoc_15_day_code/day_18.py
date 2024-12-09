"""Code to solve puzzle for day 18"""
import os


def solve():
    """Solves the day"""
    file_loc = "inputs/day18.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY18':
            print("Invalid input file header: Day18")
            return ''

        return input_file.read()
    else:
        print("Day 18 input file does not exist")
        return ''


def step_grid(grid_in, corners_on=False):
    grid_h = len(grid_in)
    grid_w = len(grid_in[0])

    new_grid = [["" for c in range(grid_w)] for l in range(grid_h)]

    def is_valid(x, y):
        return x >= 0 and x < grid_w and y >= 0 and y < grid_h

    def check_grid(x, y):
        num_lights = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    check_x = x + i
                    check_y = y + j
                    if is_valid(check_x, check_y):
                        if grid_in[check_x][check_y] == '#':
                            num_lights += 1

        if grid_in[x][y] == '#':
            if num_lights in [2, 3]:
                new_grid[x][y] = '#'
            else:
                new_grid[x][y] = '.'
        else:
            if num_lights == 3:
                new_grid[x][y] = '#'
            else:
                new_grid[x][y] = '.'

    for x in range(grid_w):
        for y in range(grid_h):
            check_grid(x, y)

    if corners_on:
        new_grid[0][0] = '#'
        new_grid[0][-1] = '#'
        new_grid[-1][0] = '#'
        new_grid[-1][-1] = '#'

    return new_grid


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 18 Puzzle 1 - NO INPUTS")
    else:
        grid = [list(l) for l in inputs.split('\n')]

        step_num = 100

        for i in range(step_num):
            print(f'Completed {round(i/step_num*100,2)}% steps', end='\r')
            grid = step_grid(grid)

        output = sum([l.count('#') for l in grid])

        print("Day 18 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 18 Puzzle 2 - NO INPUTS")
    else:
        grid = [list(l) for l in inputs.split('\n')]

        step_num = 100

        for i in range(step_num):
            print(f'Completed {round(i/step_num*100,2)}% steps', end='\r')
            grid = step_grid(grid, corners_on=True)

        output = sum([l.count('#') for l in grid])

        print("Day 18 Puzzle 2 Solution - " + str(output))
