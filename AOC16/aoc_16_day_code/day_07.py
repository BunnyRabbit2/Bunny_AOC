import os

def solve():
    file_loc = "inputs/day07.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC16_INPUT_DAY07':
            print("Invalid input file header: Day07")
            return False
     
        return file.read()
    else:
        print("Day 07 input file does not exist")

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    output = 0

    print(f'Day 07 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    output = 0

    print(f'Day_07 Puzzle 2 Solution - {output}')
    