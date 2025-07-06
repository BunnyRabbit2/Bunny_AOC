"""Code to solve puzzle for day 08"""
import os

def solve():
    """Solves the day"""
    file_loc = "inputs/day08.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC16_INPUT_DAY08':
            print("Invalid input file header: Day08")
            return ''
     
        return input_file.read()
    else:
        print("Day 08 input file does not exist")
        return ''
    
def add_lights(grid_in, a, b):
    for xv in range(a):
        for yv in range(b):
            grid_in[yv][xv] = '#'

    return grid_in

def rotate_x(grid_in, a, b):
    grid_out = [[x for x in y] for y in grid_in]

    shift = b % 6

    for bv in range(6):
        grid_out[bv][a] = grid_in[bv - shift][a]

    return grid_out

def rotate_y(grid_in, a, b):
    grid_out = [[x for x in y] for y in grid_in]

    shift = b % 50

    for bv in range(50):
        grid_out[a][bv] = grid_in[a][bv - shift]

    return grid_out

def print_panel(grid_in):
    for y in range(6):
        print(' '.join(grid_in[y]))
    
def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 08 Puzzle 1 - NO INPUTS")
    else:
        inputs = inputs.split('\n')

        output = 0

        light_panel = [['.' for x in range(50)] for y in range(6)]

        for l in inputs:
            ins = l.split(' ')

            if ins[0] == 'rect':
                a, b = [int(v) for v in ins[1].split('x')]

                light_panel = add_lights(light_panel, a, b)
            else:
                a = int(ins[2].split('=')[-1])
                b = int(ins[-1])

                if ins[1] == 'row':
                    light_panel = rotate_y(light_panel, a, b)
                else:
                    light_panel = rotate_x(light_panel, a, b)
            
            # print(''.join(['%02d'%i for i in range(50)]))
            # print_panel(light_panel)
            # print('')

        
        print_panel(light_panel)

        output = sum([sum([1 for x in y if x == '#']) for y in light_panel])

        print("Day 08 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 08 Puzzle 2 - NO INPUTS")
    else:
        output = 0

        print("Day 08 Puzzle 2 Solution - " + str(output))
    