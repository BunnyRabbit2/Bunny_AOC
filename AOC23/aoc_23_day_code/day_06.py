import os
import re
import math

def solve():
    file_loc = "inputs/day06.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC23_INPUT_DAY06':
            print("Invalid input file header: Day06")
            return False
     
        return file.read()
    else:
        print("Day 06 input file does not exist")

def gen_race_data(input_lines):
    fetch_numbers = re.compile(r'(\d+)')

    race_times = [int(v) for v in fetch_numbers.findall(input_lines[0])]
    race_dist = [int(v) for v in fetch_numbers.findall(input_lines[1])]

    race_data = list(zip(race_times, race_dist))

    return race_data

def run_race_check(race_time, race_distance):
    race_distances = [(i, i * (race_time - i)) for i in range(race_time)]

    record_beaters = [i[0] for i in race_distances if i[1] > race_distance]

    return record_beaters

def gen_race_data_alt(input_lines):
    fetch_numbers = re.compile(r'(\d+)')

    race_time = ''.join(fetch_numbers.findall(input_lines[0]))
    race_dist = ''.join(fetch_numbers.findall(input_lines[1]))

    return (int(race_time), int(race_dist))

def run_race_check_alt(race_time, race_distance):
    min_time = (race_time - math.sqrt(race_time * race_time - 4 * race_distance)) / 2
    max_time = (race_time + math.sqrt(race_time * race_time - 4 * race_distance)) / 2

    return (math.ceil(min_time), math.floor(max_time))

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return
    
    output = 1

    race_data = gen_race_data(inputs.splitlines())
    for race in race_data:
        record_beaters = run_race_check(race[0], race[1])
        output *= len(record_beaters)

    print(f'Day 06 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    race_data = gen_race_data_alt(inputs.splitlines())

    record_beaters = run_race_check_alt(race_data[0], race_data[1])

    output = record_beaters[1] - record_beaters[0] + 1

    print(f'Day_06 Puzzle 2 Solution - {output}')
    