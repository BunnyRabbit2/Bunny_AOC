import os
import re
import math

def solve():
    file_loc = "inputs/day08.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC23_INPUT_DAY08':
            print("Invalid input file header: Day08")
            return False
     
        return file.read()
    else:
        print("Day 08 input file does not exist")

def gen_route_map(input_lines):
    route_line = input_lines[0]

    pos_search = re.compile(r'([A-Z]{3})')
    routes = input_lines[2:]

    start_nodes = []

    route_map = {}
    for r in routes:
        pos_list = pos_search.findall(r)
        route_map[pos_list[0]] = {
            'L': pos_list[1],
            'R': pos_list[2]
        }
        if pos_list[0].endswith('A'):
            start_nodes.append(pos_list[0])

    return (route_line, route_map, start_nodes)

def run_route(start_node, end_node_char, route, route_map):
    route_pos = 0
    steps = 0

    next_node = start_node

    while True:
        steps += 1
        next_node = route_map[next_node][route[route_pos]]
        route_pos += 1
        if route_pos >= len(route): route_pos = 0
        if next_node[2] == end_node_char: break

    return (steps, next_node)

def run_loop_route(start_node, route, route_map):
    route_pos = 0
    steps = 0

    next_node = start_node

    while True:
        steps += 1
        next_node = route_map[next_node][route[route_pos]]
        route_pos += 1
        if route_pos >= len(route): route_pos = 0
        if next_node == start_node: break

    return steps

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    route_map = gen_route_map(inputs.splitlines())

    output = run_route('AAA', 'Z', route_map[0], route_map[1])[0]

    print(f'Day 08 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return
    
    route_map = gen_route_map(inputs.splitlines())

    start_nodes = route_map[2]

    step_counts = []

    for node in start_nodes:
        step_counts.append(run_route(node, 'Z', route_map[0], route_map[1])[0])

    output = math.lcm(*step_counts)

    print(f'Day_08 Puzzle 2 Solution - {output}')
    