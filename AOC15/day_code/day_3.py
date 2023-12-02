import os


def solve():
    file_loc = "inputs/day3.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read()
    else:
        print("Day 3 input file does not exist")


def move(command):
    move_x = move_y = 0
    if command == '<':
        move_x -= 1
    elif command == '^':
        move_y += 1
    elif command == '>':
        move_x += 1
    elif command == 'v':
        move_y -= 1

    return (move_x, move_y)


def process_route(route):
    current_x = 0
    current_y = 0
    houses = []
    houses.append((current_x, current_y))

    for h in route:
        m = move(h)
        current_x += m[0]
        current_y += m[1]

        if (current_x, current_y) not in houses:
            houses.append((current_x, current_y))

    return len(houses)


def process_route_alt(route):
    santa_x = 0
    santa_y = 0
    robo_santa_x = 0
    robo_santa_y = 0
    houses = []
    houses.append((santa_x, santa_y))
    move_robo_santa = False

    for h in route:
        m = move(h)

        if move_robo_santa:
            robo_santa_x += m[0]
            robo_santa_y += m[1]

            if (robo_santa_x, robo_santa_y) not in houses:
                houses.append((robo_santa_x, robo_santa_y))

            move_robo_santa = False
        else:
            santa_x += m[0]
            santa_y += m[1]

            if (santa_x, santa_y) not in houses:
                houses.append((santa_x, santa_y))

            move_robo_santa = True

    return len(houses)


def solve_puzzle_1(file_location):
    input = load_inputs(file_location)

    output = process_route(input)

    print(f'Day 3 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    input = load_inputs(file_location)

    output = process_route_alt(input)

    print(f'Day 3 Puzzle 2 Solution - {output}')
