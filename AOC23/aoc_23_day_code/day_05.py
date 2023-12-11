import os

def solve():
    file_loc = "inputs/day05.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC23_INPUT_DAY05':
            print("Invalid input file header: Day05")
            return False
     
        return file.read()
    else:
        print("Day 05 input file does not exist")

def gen_almanac(input_sets: list[str]):
    almanac = {
        'seed_numbers': [],
        'seed_ranges': [],
        'run_order': [
            'seed-to-soil',
            'soil-to-fertilizer',
            'fertilizer-to-water',
            'water-to-light',
            'light-to-temperature',
            'temperature-to-humidity',
            'humidity-to-location'
        ],
        'seed-to-soil': {},
        'soil-to-fertilizer': {},
        'fertilizer-to-water': {},
        'water-to-light': {},
        'light-to-temperature': {},
        'temperature-to-humidity': {},
        'humidity-to-location': {}
    }

    for almanac_set in input_sets:
        if almanac_set.startswith('seeds'):
            seed_numbers = almanac_set.split(':')[-1].split()
            seed_numbers = [int(seed_num) for seed_num in seed_numbers]

            almanac['seed_numbers'] = seed_numbers

            seed_num_starts = [int(seed_num) for x, seed_num in enumerate(seed_numbers) if x % 2 == 0]
            seed_num_ranges = [int(seed_num) for x, seed_num in enumerate(seed_numbers) if x % 2 == 1]

            almanac['seed_ranges'] = [(range_start, seed_num_ranges[x]) for x, range_start in enumerate(seed_num_starts)]
        else:
            set_split = almanac_set.split(':\n')
            almanac_name = set_split[0].split()[0]
            map_sets = set_split[1].split('\n')

            for map_set in map_sets:
                map_set_split = map_set.split()
                destination = int(map_set_split[0])
                source = int(map_set_split[1])
                set_range = int(map_set_split[2])

                map_key = (source, source + set_range - 1)

                almanac[almanac_name][map_key] = destination - source

    return almanac

def get_mapped_number(seed_number, almanac, check_type):
    for range_key in almanac[check_type]:
        if range_key[0] <= seed_number <=range_key[1]:
            return seed_number + almanac[check_type][range_key]
    return seed_number

def run_seed_number(seed_number, almanac):
    run_order = almanac['run_order']

    num_out = seed_number

    for map_check in run_order:
        num_out = get_mapped_number(num_out, almanac, map_check)

    return num_out

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    input_sets = inputs.split('\n\n')

    almanac = gen_almanac(input_sets)

    seed_locations = [run_seed_number(seed_num, almanac) for seed_num in almanac['seed_numbers']]

    output = min(seed_locations)

    print(f'Day 05 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    input_sets = inputs.split('\n\n')

    almanac = gen_almanac(input_sets)

    seed_locations = []

    for seed_range in almanac['seed_ranges']:
        seed_start = seed_range[0]
        for i in range(seed_range[1]):
            seed_locations.append(run_seed_number(seed_start + i, almanac))

    output = min(seed_locations)

    print(f'Day_05 Puzzle 2 Solution - {output}')
    