import os


def solve():
    file_loc = "inputs/day7.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.readlines()
    else:
        print("Day 7 input file does not exist")


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def create_gate_list(inputs):
    gate_list = {}

    for c in inputs:
        in_wire_1 = "NIL"
        in_wire_2 = "NIL"
        gate_t = "T0"
        gate_v = None

        output = c.split("->")[1].strip()
        command = c.split("->")[0].split()
        if len(command) == 1:
            in_wire_1 = command[0]
            gate_t = "DIODE"
        elif command[1] == "AND":
            in_wire_1 = command[0]
            in_wire_2 = command[2]
            gate_t = command[1]
        elif command[1] == "OR":
            in_wire_1 = command[0]
            in_wire_2 = command[2]
            gate_t = command[1]
        elif command[0] == "NOT":
            in_wire_1 = command[1]
            gate_t = command[0]
        elif command[1] == "LSHIFT":
            in_wire_1 = command[0]
            gate_t = command[1]
            gate_v = int(command[2])
        elif command[1] == "RSHIFT":
            in_wire_1 = command[0]
            gate_t = command[1]
            gate_v = int(command[2])

        gate_list[output] = {
            "type": gate_t,
            "value": gate_v,
            "in_wire_1": in_wire_1,
            "in_wire_2": in_wire_2,
            "out_signal": None,
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
    in_wire_2_output = -1

    in_wire_1_output = gate_list[gate_0["in_wire_1"]]["out_signal"]
    if gate_0["in_wire_2"] != "NIL":
        in_wire_2_output = gate_list[gate_0["in_wire_2"]]["out_signal"]

    if gate_0["type"] == "DIODE":
        out = in_wire_1_output
    elif gate_0["type"] == "AND":
        out = in_wire_1_output & in_wire_2_output
    elif gate_0["type"] == "OR":
        out = in_wire_1_output | in_wire_2_output
    elif gate_0["type"] == "NOT":
        out = ~in_wire_1_output
    elif gate_0["type"] == "LSHIFT":
        out = in_wire_1_output << gate_0["value"]
    elif gate_0["type"] == "RSHIFT":
        out = in_wire_1_output >> gate_0["value"]

    gate_0["out_signal"] = out


def calculateOut(gate, gate_list):
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
    in_wire_2_output = -1

    in_wire_1_output = gate_list[gate_0["in_wire_1"]]["out_signal"]
    if gate_0["in_wire_2"] != "NIL":
        in_wire_2_output = gate_list[gate_0["in_wire_2"]]["out_signal"]

    if gate_0["type"] == "DIODE":
        out = in_wire_1_output
    elif gate_0["type"] == "AND":
        out = in_wire_1_output & in_wire_2_output
    elif gate_0["type"] == "OR":
        out = in_wire_1_output | in_wire_2_output
    elif gate_0["type"] == "NOT":
        out = ~in_wire_1_output
    elif gate_0["type"] == "LSHIFT":
        out = in_wire_1_output << gate_0["value"]
    elif gate_0["type"] == "RSHIFT":
        out = in_wire_1_output >> gate_0["value"]

    gate_0["out_signal"] = out


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)
    gate_list = create_gate_list(inputs)

    calculateOut("a", gate_list)

    output = gate_list["a"]

    print(f'Day 7 Puzzle 2 Solution - {output["out_signal"]}')


def solve_puzzle_2(file_location):
    # inputs = load_inputs(file_location)

    output = (0, 0)

    print(f'Day 7 Puzzle 2 Solution - {output[1]}')
