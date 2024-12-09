"""Code to solve puzzle for day 06"""
import os
from re import findall

def solve():
    """Solves the day"""
    file_loc = "inputs/day06.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY06':
            print("Invalid input file header: Day06")
            return ''
     
        return input_file.read()
    else:
        print("Day 06 input file does not exist")
        return ''

def process_light_commands(input_commands, alt_process):
    commands = findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", input_commands)

    lights = [[0 for i in range(1000)] for j in range(1000)]

    for command, x1, y1, x2, y2 in commands:
        coords = [(x,y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)]
        for x,y in coords:
            if command == "turn on":
                if alt_process:
                    lights[x][y] += 1
                else:
                    lights[x][y] = 1
            elif command == "turn off":
                if alt_process:
                    lights[x][y] -= 1
                    if lights[x][y] < 0:
                        lights[x][y] = 0
                else:
                    lights[x][y] = 0
            elif command == "toggle":
                if alt_process:
                    lights[x][y] += 2
                else:
                    if lights[x][y] == 1:
                        lights[x][y] = 0
                    else:
                        lights[x][y] = 1

    return lights

def count_lights_on(field):
    """Counts the number of lights on in a given field"""
    size = len(field)
    lights_on = 0

    for x in range(size):
        for y in range(size):
            if field[x][y] == 1:
                lights_on += 1

    return lights_on

def count_brightness(field):
    """Counts the total brightness of the lights on in a given field"""
    size = len(field)
    total_brightness = 0

    for x in range(size):
        for y in range(size):
            total_brightness += field[x][y]

    return total_brightness

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 06 Puzzle 1 - NO INPUTS")
    else:
        output = count_lights_on(process_light_commands(inputs, False))

        print("Day 06 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 06 Puzzle 2 - NO INPUTS")
    else:
        output = count_brightness(process_light_commands(inputs, True))

        print("Day 06 Puzzle 2 Solution - " + str(output))
    