import os


def solve():
    file_loc = "inputs/day1.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read()
    else:
        print("Day 1 input file does not exist")


def process_inputs(inputs):
    current_floor = 0
    has_entered_basement = False
    when_entered_basement = 1

    for c in inputs:
        if c == '(':
            current_floor += 1
        elif c == ')':
            current_floor -= 1
        if not has_entered_basement:
            if current_floor < 0:
                has_entered_basement = True
            else:
                when_entered_basement += 1

    return (current_floor, when_entered_basement)


def solve_puzzle_1(file_location):
    output = process_inputs(load_inputs(file_location))

    print(f'Day 1 Puzzle 1 Solution - {output[0]}')


def solve_puzzle_2(file_location):
    output = process_inputs(load_inputs(file_location))

    print(f'Day 1 Puzzle 2 Solution - {output[1]}')
