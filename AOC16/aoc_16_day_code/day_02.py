import os

def solve():
    file_loc = "inputs/day02.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC16_INPUT_DAY02':
            print("Invalid input file header: Day02")
            return False
     
        return file.read()
    else:
        print("Day 02 input file does not exist")

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return
    
    keypad = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    x_pos = 1
    y_pos = 1

    keypad_lines = inputs.split('\n')

    keypad_code = []
    line_strs = []

    for line in keypad_lines:
        out_line = []
        for c in line:
            if c == 'U' and y_pos > 0: y_pos -= 1
            elif c == 'D' and y_pos < 2: y_pos += 1
            elif c == 'L' and x_pos > 0: x_pos -= 1
            elif c == 'R' and x_pos < 2: x_pos += 1
            out_line.append(f'{c}{keypad[y_pos][x_pos]}')
        line_strs.append('|'.join(out_line))
        keypad_code.append(keypad[y_pos][x_pos])

    output = keypad_code

    print(f'Day 02 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return
    
    keypad = [
        [ 0 , 0 , 1 , 0 , 0 ],
        [ 0 , 2 , 3 , 4 , 0 ],
        [ 5 , 6 , 7 , 8 , 9 ],
        [ 0 ,'A','B','C', 0 ],
        [ 0 , 0 ,'D', 0 , 0 ]
    ]

    x_pos = 0
    y_pos = 2

    keypad_lines = inputs.split('\n')

    keypad_code = []
    line_strs = []

    for line in keypad_lines:
        out_line = []
        for c in line:
            if c == 'U' and y_pos > 0:
                if keypad[y_pos - 1][x_pos] != 0: y_pos -= 1
            elif c == 'D' and y_pos < 4:
                if keypad[y_pos + 1][x_pos] != 0: y_pos += 1
            elif c == 'L' and x_pos > 0:
                if keypad[y_pos][x_pos - 1] != 0: x_pos -= 1
            elif c == 'R' and x_pos < 4:
                if keypad[y_pos][x_pos + 1] != 0: x_pos += 1
            out_line.append(f'{c}{keypad[y_pos][x_pos]}')
        line_strs.append('|'.join(out_line))
        keypad_code.append(keypad[y_pos][x_pos])

    output = keypad_code

    print(f'Day_02 Puzzle 2 Solution - {output}')
    