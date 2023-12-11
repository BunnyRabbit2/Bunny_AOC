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

            seed_num_starts = seed_numbers[::2]
            seed_num_ranges = seed_numbers[1::2]

            almanac['seed_ranges'] = list(zip(seed_num_starts, seed_num_ranges))

            new_seed_ranges = []

            for seed_range in almanac['seed_ranges']:
                new_seed_ranges.append((seed_range[0], seed_range[0] + seed_range[1] - 1))
            
            almanac['seed_ranges'] = new_seed_ranges
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
        if range_key[0] <= seed_number <= range_key[1]:
            return seed_number + almanac[check_type][range_key]
    return seed_number

def run_seed_number(seed_number, almanac):
    run_order = almanac['run_order']

    num_out = seed_number

    for map_check in run_order:
        num_out = get_mapped_number(num_out, almanac, map_check)

    return num_out

def get_mapped_range(seed_range, almanac, check_type):

    check_ranges = almanac[check_type].keys()
    check_ranges = sorted(check_ranges, key = lambda x: x[0])

    new_seed_ranges = []

    for check_range in check_ranges:
        if check_range[0] <= seed_range[0] <= check_range[1]:
            modifier = almanac[check_type][check_range]
            if seed_range[1] <= check_range[1]:
                new_seed_ranges.append((seed_range[0] + modifier, seed_range[1] + modifier))
            else:
                new_seed_ranges.append((seed_range[0] + modifier, check_range[1] + modifier))
                new_seed_ranges.extend(get_mapped_range((check_range[1] + 1, seed_range[1]), almanac, check_type))

    return new_seed_ranges

def run_seed_range(seed_range, almanac):
    run_order = almanac['run_order']

    map_ranges_out = [seed_range]

    for map_check in run_order:
        next_map_ranges = []
        for check_range in map_ranges_out:
            next_map_ranges.extend(get_mapped_range(check_range, almanac, map_check))
        map_ranges_out = next_map_ranges

    return map_ranges_out

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

    seed_location_ranges = []

    for seed_range in almanac['seed_ranges']:
        seed_location_ranges.extend(run_seed_range(seed_range, almanac))

    output = min([loc_range[0] for loc_range in seed_location_ranges])

    print(f'Day_05 Puzzle 2 Solution - {output}')
    