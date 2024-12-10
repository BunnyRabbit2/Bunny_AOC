"""Code to solve puzzle for day 03"""
import os


def solve():
    """Solves the day"""
    file_loc = "inputs/day03.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC16_INPUT_DAY03':
            print("Invalid input file header: Day03")
            return ''

        return input_file.read()
    else:
        print("Day 03 input file does not exist")
        return ''


def is_good_triangle(tri_points):
    if len(tri_points) != 3:
        return False

    return tri_points[0] + tri_points[1] > tri_points[2] and tri_points[1] + tri_points[2] > tri_points[0] and tri_points[2] + tri_points[0] > tri_points[1]


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 03 Puzzle 1 - NO INPUTS")
    else:
        triangles = [[int(n) for n in l.split()] for l in inputs.split('\n')]

        output = sum([1 if is_good_triangle(t) else 0 for t in triangles])

        print("Day 03 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 03 Puzzle 2 - NO INPUTS")
    else:
        data_rows = [[int(n) for n in l.split()] for l in inputs.split('\n')]

        triangles = []

        for i in range(0, len(data_rows), 3):
            for t in range(3):
                triangles.append((data_rows[i][t], data_rows[i+1][t], data_rows[i+2][t]))

        output = sum([1 if is_good_triangle(t) else 0 for t in triangles])

        print("Day 03 Puzzle 2 Solution - " + str(output))
