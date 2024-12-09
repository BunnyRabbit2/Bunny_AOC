"""Code to solve puzzle for day 20"""
import os

def solve():
    """Solves the day"""
    file_loc = "inputs/day20.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY20':
            print("Invalid input file header: Day20")
            return ''
     
        return input_file.read()
    else:
        print("Day 20 input file does not exist")
        return ''

    
def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 20 Puzzle 1 - NO INPUTS")
    else:
        inputs = int(inputs)

        house_num = 1000000

        output = 0

        houses = []
        for i in range(house_num):
            houses.append(0)

        for i in range(1, len(houses)):
            for j in range(i, len(houses), i):
                houses[j] += i * 10

        for i in range(1, len(houses)):
            if houses[i] >= inputs:
                output = i
                break

        print(f'Day 20 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 20 Puzzle 1 - NO INPUTS")
    else:
        inputs = int(inputs)

        house_num = 1000000

        output = 0

        houses = []
        for i in range(house_num):
            houses.append(0)

        for i in range(1, len(houses)):
            house_count = 0
            for j in range(i, len(houses), i):
                houses[j] += i * 11
                house_count += 1
                if house_count >= 50:
                    break

        for i in range(1, len(houses)):
            if houses[i] >= inputs:
                output = i
                break

        print(f'Day 20 Puzzle 2 Solution - {output}')