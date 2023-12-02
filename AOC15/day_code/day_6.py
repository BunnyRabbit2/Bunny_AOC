import os
from PIL import Image
import numpy as np
import re

def solve():
    file_loc = "inputs/day6.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read()
    else:
        print("Day 6 input file does not exist")

def create_commands(command_strings):
    # command = ["on/off/toggle", (0,0), (1,1)] EXAMPLE COMMAND
    commands = []

    for l in command_strings:
        c_split = l.split()
        new_command = []
        first_c_pos = second_c_pos = 0

        if c_split[0] == "toggle":
            new_command.append("toggle")
            first_c_pos = 1
            second_c_pos = 3
        elif c_split[0] == "turn":
            first_c_pos = 2
            second_c_pos = 4
            if c_split[1] == "on":
                new_command.append("on")
            elif c_split[1] == "off":
                new_command.append("off")
        
        first_com_split = c_split[first_c_pos].split(",")
        second_com_split = c_split[second_c_pos].split(",")

        new_command.append((int(first_com_split[0]), int(first_com_split[1])))
        new_command.append((int(second_com_split[0]), int(second_com_split[1])))

        commands.append(new_command)
    
    return commands

def count_lights_on(field):
    size = len(field)
    lights_on = 0

    for x in range(size):
        for y in range(size):
            if field[x][y] == 1:
                lights_on += 1

    return lights_on

def count_brightness(field):
    size = len(field)
    total_brightness = 0

    for x in range(size):
        for y in range(size):
            total_brightness += field[x][y]

    return total_brightness

def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    commands = re.findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", inputs)
    lights = [[0 for i in range(1000)] for j in range(1000)]

    for command, x1, y1, x2, y2 in commands:
        coords = [(x,y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)]
        for x,y in coords:
            if command == "turn on":
                lights[x][y] = 1
            elif command == "turn off":
                lights[x][y] = 0
            elif command == "toggle":
                if lights[x][y] == 1:
                    lights[x][y] = 0
                else:
                    lights[x][y] = 1

    output = count_lights_on(lights)

    Image.fromarray(np.array(lights)).save("lights.png")

    print(f'Day 6 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    commands = re.findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", inputs)
    lights = [[0 for i in range(1000)] for j in range(1000)]

    for command, x1, y1, x2, y2 in commands:
        coords = [(x,y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)]
        for x,y in coords:
            if command == "turn on":
                lights[x][y] += 1
            elif command == "turn off":
                lights[x][y] -= 1
                if lights[x][y] < 0:
                    lights[x][y] = 0
            elif command == "toggle":
                lights[x][y] += 2

    output = count_brightness(lights)

    print(f'Day 6 Puzzle 2 Solution - {output}')