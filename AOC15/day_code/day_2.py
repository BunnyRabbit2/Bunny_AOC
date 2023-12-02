import os


def solve():
    file_loc = "inputs/day2.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split()
    else:
        print("Day 2 input file does not exist")


def calculate_wrapping(l, w, h):
    side_1 = l*w
    side_2 = l*h
    side_3 = w*h

    smallest_side = min(side_1, side_2, side_3)

    surface_area = 2*side_1 + 2*side_2 + 2*side_3

    return surface_area + smallest_side


def calculate_ribbon(l, w, h):
    per_1 = l*2 + w*2
    per_2 = l*2 + h*2
    per_3 = w*2 + h*2

    ribbon = min(per_1, per_2, per_3)
    bow = l*w*h

    return ribbon+bow


def get_lwh_from_string(stringLwh):
    values = stringLwh.split('x')
    l = int(values[0])
    w = int(values[1])
    h = int(values[2])

    return (l, w, h)


def calculate_total_sf(inputs):
    total_wrapping_sf = 0
    total_ribbon_f = 0

    for s in inputs:
        values = get_lwh_from_string(s)
        total_wrapping_sf += calculate_wrapping(
            values[0], values[1], values[2])
        total_ribbon_f += calculate_ribbon(values[0], values[1], values[2])

    return (total_wrapping_sf, total_ribbon_f)


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    output = calculate_total_sf(inputs)

    print(f'Day 2 Puzzle 1 Solution - {output[0]}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    output = calculate_total_sf(inputs)

    print(f'Day 2 Puzzle 2 Solution - {output[1]}')
