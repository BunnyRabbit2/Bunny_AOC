"""Code to solve puzzle for day 07"""

# NEEDS SOLVING

import os

def solve():
    """Solves the day"""
    file_loc = "inputs/day07.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY07':
            print("Invalid input file header: Day07")
            return ''
     
        return input_file.read()
    else:
        print("Day 07 input file does not exist")
        return ''

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def create_gate_list(inputs):
    gate_list = {}

    for c in inputs:
        in_wire = "NIL"
        in_wire_2 = "NIL"
        gate_t = "T0"
        gate_v = None

        output = c.split("->")[1].strip()
        command = c.split("->")[0].split()
        if len(command) == 1:
            in_wire = command[0]
            gate_t = "DIODE"
        elif command[1] == "AND":
            in_wire = command[0]
            in_wire_2 = command[2]
            gate_t = command[1]
        elif command[1] == "OR":
            in_wire = command[0]
            in_wire_2 = command[2]
            gate_t = command[1]
        elif command[0] == "NOT":
            in_wire = command[1]
            gate_t = command[0]
        elif command[1] == "LSHIFT":
            in_wire = command[0]
            gate_t = command[1]
            gate_v = int(command[2])
        elif command[1] == "RSHIFT":
            in_wire = command[0]
            gate_t = command[1]
            gate_v = int(command[2])

        gate_list[output] = {
            "type":gate_t,
            "value":gate_v,
            "in_wire_1":in_wire,
            "in_wire_2":in_wire_2,
            "out_signal":None,
        }

    return gate_list

def calculate_in(gate, gate_list):
    gate_0 = gate_list[gate]

    if is_int(gate_0["in_wire_1"]):
        gate_0["out_signal"] = int(gate_0["in_wire_1"])
        return

    if gate_list[gate_0["in_wire_1"]]["out_signal"] == None:
        calculate_in(gate_0["in_wire_1"], gate_list)
    if gate_0["in_wire_2"] != "NIL":
        if gate_list[gate_0["in_wire_2"]]["out_signal"] == None:
            calculate_in(gate_0["in_wire_2"], gate_list)

    out = -1
    iw2o = -1

    iw1o = gate_list[gate_0["in_wire_1"]]["out_signal"]
    if gate_0["in_wire_2"] != "NIL":
        iw2o = gate_list[gate_0["in_wire_2"]]["out_signal"]

    if gate_0["type"] == "DIODE":
        out = iw1o
    elif gate_0["type"] == "AND":
        out = iw1o & iw2o
    elif gate_0["type"] == "OR":
        out = iw1o | iw2o
    elif gate_0["type"] == "NOT":
        out = ~iw1o
    elif gate_0["type"] == "LSHIFT":
        out = iw1o << gate_0["value"]
    elif gate_0["type"] == "RSHIFT":
        out = iw1o >> gate_0["value"]

    gate_0["out_signal"] = out

def calculate_out(gate, gate_list):
    gateO = gate_list[gate]

    if is_int(gateO["in_wire_1"]):
        gateO["out_signal"] = int(gateO["in_wire_1"])
        return

    if gate_list[gateO["in_wire_1"]]["out_signal"] == None:
        calculate_in(gateO["in_wire_1"], gate_list)
    if gateO["in_wire_2"] != "NIL":
        if gate_list[gateO["in_wire_2"]]["out_signal"] == None:
            calculate_in(gateO["in_wire_2"], gate_list)

    out = -1
    iw2o = -1

    iw1o = gate_list[gateO["in_wire_1"]]["out_signal"]
    if gateO["in_wire_2"] != "NIL":
        iw2o = gate_list[gateO["in_wire_2"]]["out_signal"]

    if gateO["type"] == "DIODE":
        out = iw1o
    elif gateO["type"] == "AND":
        out = iw1o & iw2o
    elif gateO["type"] == "OR":
        out = iw1o | iw2o
    elif gateO["type"] == "NOT":
        out = ~iw1o
    elif gateO["type"] == "LSHIFT":
        out = iw1o << gateO["value"]
    elif gateO["type"] == "RSHIFT":
        out = iw1o >> gateO["value"]

    gateO["out_signal"] = out

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 07 Puzzle 1 - NO INPUTS")
    else:
        gate_list = create_gate_list(inputs.split('\n'))

        calculate_out("a", gate_list)

        output = gate_list["a"]['out_signal']

        print("Day 07 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 07 Puzzle 2 - NO INPUTS")
    else:
        output = 0

        print("Day 07 Puzzle 2 Solution - " + str(output))
    