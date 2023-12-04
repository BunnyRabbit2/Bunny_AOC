import os

def solve():
    file_loc = "inputs/day01.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC16_INPUT_DAY01':
            print("Invalid input file header: Day01")
            return False
     
        return file.read()
    else:
        print("Day 01 input file does not exist")

def find_distance_to_base(steps):
    pos_stack = []
    found_ans_2 = False
    ans_2 = (0,0)

    x,y = 0,0
    direction = 0 # 0 N, 1 E, 2 S, 3 W
    def turn_right(d):
        d += 1
        if d > 3: d = 0
        return d
    def turn_left(d):
        d -= 1
        if d < 0: d = 3
        return d

    for c in steps:
        if c[0] == 'L':
            direction = turn_left(direction)
        elif c[0] == 'R':
            direction = turn_right(direction)

        for _ in range(int(c[1:])):
            if direction == 0: y += 1
            elif direction == 1: x += 1
            elif direction == 2: y -= 1
            elif direction == 3: x -= 1

            if (x,y) in pos_stack and not found_ans_2:
                ans_2 = abs(x)+abs(y)
                found_ans_2 = True
            else:
                pos_stack.append((x,y))

    return (abs(x)+abs(y),ans_2)

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    output = find_distance_to_base(inputs.split(', '))[0]

    print(f'Day 01 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    output = find_distance_to_base(inputs.split(', '))[1]

    print(f'Day_01 Puzzle 2 Solution - {output}')
    