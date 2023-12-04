import os


def solve():
    file_loc = "inputs/day03.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC23_INPUT_DAY03':
            print("Invalid input file header: Day03")
            return False

        return file.read()
    else:
        print("Day 03 input file does not exist")


def create_schematic_grid(input_lines: list[str]):
    schematic_grid = [
        [c for c in l] for l in input_lines
    ]

    return schematic_grid


def check_number(x_pos_list: list, y_pos: int, schematic: list[list[str]]):
    is_part_number = False
    is_gear_part = False
    gear_loc = None

    part_number = []

    for x_pos in x_pos_list:
        # print(f'----- {x_pos},{y_pos}: {schematic[y_pos][x_pos]}')
        part_number.append(schematic[y_pos][x_pos])
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                x_check = x_pos + x
                y_check = y_pos + y
                if x_check >= 0 and x_check < len(schematic[0]) and y_check >= 0 and y_check < len(schematic):
                    check_char = schematic[y_pos + y][x_pos + x]
                    if check_char != '.' and not check_char.isdigit():
                        is_part_number = True
                        if check_char == '*':
                            is_gear_part = True
                            gear_loc = (x_check, y_check)
                    # print(f'{x_pos + x},{y_pos + y}: {check_char}')

    if is_part_number:
        part_number = int(''.join(part_number))
        return (part_number, is_gear_part, gear_loc)
    else:
        return (0, is_gear_part, gear_loc)


def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    schematic_grid = create_schematic_grid(inputs.split('\n'))

    part_numbers = []

    for y, line in enumerate(schematic_grid):
        line_len = len(line)
        x = 0
        while x < line_len:
            char = line[x]
            if char.isdigit():
                number_check = [x]
                while x < len(line) - 1 and line[x + 1].isdigit():
                    number_check.append(x + 1)
                    x += 1
                part_numbers.append(check_number(
                    number_check, y, schematic_grid)[0])
            x += 1

    output = sum(part_numbers)

    print(f'Day 03 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return
    
    schematic_grid = create_schematic_grid(inputs.split('\n'))

    maybe_gear_parts = {}

    for y, line in enumerate(schematic_grid):
        line_len = len(line)
        x = 0
        while x < line_len:
            char = line[x]
            if char.isdigit():
                number_check = [x]
                while x < len(line) - 1 and line[x + 1].isdigit():
                    number_check.append(x + 1)
                    x += 1
                part_check = check_number(number_check, y, schematic_grid)

                if part_check[1]:
                    maybe_gear_parts.setdefault(part_check[2], []).append(part_check[0])
            x += 1

    gear_parts = {gear_loc: part_numbers for gear_loc, part_numbers in maybe_gear_parts.items() if len(part_numbers) ==2}

    gear_ratios = [part_numbers[0] * part_numbers[1] for part_numbers in gear_parts.values()]

    output = sum(gear_ratios)

    print(f'Day_03 Puzzle 2 Solution - {output}')
