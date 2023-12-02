import os
import errno

try:
    os.makedirs("output/d18/")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


def solve():
    file_loc = "inputs/day18.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split('\n')
    else:
        print("Day 18 input file does not exist")


def create_grid(inputs, width):
    grid = []
    for x in range(width):
        column = []
        for y in range(width):
            column.append("")
        grid.append(column)

    for y in range(len(inputs)):
        line = list(inputs[y])
        for x in range(len(line)):
            grid[x][y] = line[x]

    return grid


def step_light_grid(grid, corners_on=False):
    size = len(grid)
    new_grid = []
    for x in range(size):
        column = []
        for y in range(size):
            column.append("")
        new_grid.append(column)

    def is_valid(x, y):
        return x >= 0 and x < size and y >= 0 and y < size

    for x in range(size):
        for y in range(size):
            to_check = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if not i == 0 or not j == 0:
                        cX = x + i
                        cY = y + j
                        if is_valid(cX, cY):
                            to_check.append((cX, cY))
            lights_on = 0
            for tC in to_check:
                if grid[tC[0]][tC[1]] == '#':
                    lights_on += 1
            if grid[x][y] == '#':
                if lights_on == 2 or lights_on == 3:
                    new_grid[x][y] = '#'
                else:
                    new_grid[x][y] = '.'
            else:
                if lights_on == 3:
                    new_grid[x][y] = '#'
                else:
                    new_grid[x][y] = '.'

    if corners_on:
        new_grid[0][0] = '#'
        new_grid[0][size-1] = '#'
        new_grid[size-1][0] = '#'
        new_grid[size-1][size-1] = '#'

    return new_grid


def count_lights_on(grid):
    size = len(grid)

    lights_on = 0

    for x in range(size):
        for y in range(size):
            if grid[x][y] == '#':
                lights_on += 1

    return lights_on


def print_grid(grid, file_suf=""):
    size = len(grid)

    lines = []
    for y in range(size):
        line = ""
        for x in range(size):
            line += grid[x][y]
        line += '\n'
        lines.append(line)
    file = open("output/d18/output" + file_suf + ".txt", "w+")
    file.writelines(lines)


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)
    grid = create_grid(inputs, 100)

    for i in range(100):
        grid = step_light_grid(grid)

    output = count_lights_on(grid)

    print(f'Day 18 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)
    grid = create_grid(inputs, 100)

    size = len(grid)

    grid[0][0] = '#'
    grid[0][size-1] = '#'
    grid[size-1][0] = '#'
    grid[size-1][size-1] = '#'

    for i in range(100):
        grid = step_light_grid(grid, True)
        # printGrid(grid, str(i))

    output = count_lights_on(grid)
    print(f'Day 18 Puzzle 2 Solution - {output}')
