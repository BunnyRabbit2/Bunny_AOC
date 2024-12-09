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
        if not first_line == 'AOC15_INPUT_DAY03':
            print("Invalid input file header: Day03")
            return ''
     
        return input_file.read()
    else:
        print("Day 03 input file does not exist")
        return ''

def move(command):
    """Returns new co-ords given the move command"""
    move_x = move_y = 0
    if command == '<':
        move_x -= 1
    elif command == '^':
        move_y += 1
    elif command == '>':
        move_x += 1
    elif command == 'v':
        move_y -= 1

    return (move_x,move_y)

def process_route(route):
    """Process the route for puzzle 1"""
    current_x = 0
    current_y = 0
    houses = []
    houses.append((current_x,current_y))

    for h in route:
        m = move(h)
        current_x += m[0]
        current_y += m[1]
        
        if (current_x,current_y) not in houses:
            houses.append((current_x,current_y))

    return len(houses)

def process_route_alt(route):
    """Process the route for puzzle 2"""
    santa_x = 0
    santa_y = 0
    robo_santa_x = 0
    robo_santa_y = 0
    houses = []
    houses.append((santa_x,santa_y))
    move_robo_santa = False

    for h in route:
        m = move(h)
        
        if move_robo_santa:
            robo_santa_x += m[0]
            robo_santa_y += m[1]

            if (robo_santa_x,robo_santa_y) not in houses:
                houses.append((robo_santa_x,robo_santa_y))

            move_robo_santa = False
        else:
            santa_x += m[0]
            santa_y += m[1]

            if (santa_x,santa_y) not in houses:
                houses.append((santa_x,santa_y))

            move_robo_santa = True

    return len(houses)

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 03 Puzzle 1 - NO INPUTS")
    else:
        output = process_route(inputs)

        print("Day 03 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 03 Puzzle 2 - NO INPUTS")
    else:
        output = process_route_alt(inputs)

        print("Day 03 Puzzle 2 Solution - " + str(output))
    