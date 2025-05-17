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
                xv, yv = [int(v) for v in ins[1].split('x')]

                for y in range(yv):
                    for x in range(xv):
                        light_panel[y][x] = '#'
            else:
                move_num = int(ins[2].split('=')[-1])
                if ins[1] == 'row':
                    pass

        for y in light_panel:
            print(''.join(y))

        print("Day 08 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 08 Puzzle 2 - NO INPUTS")
    else:
        output = 0

        print("Day 08 Puzzle 2 Solution - " + str(output))
    