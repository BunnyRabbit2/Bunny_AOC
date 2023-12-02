import os


def solve():
    file_loc = "inputs/day23.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split('\n')
    else:
        print("Day 23 input file does not exist")


def create_instruction_list(inputs):
    instructions = []
    for instruction in inputs:
        ins_split = instruction.split()
        ins_1 = ''
        ins_2 = 0

        if ins_split[1] == 'a' or ins_split[1] == 'b':
            ins_1 = ins_split[1]
        else:
            ins_1 = int(ins_split[1][1:])
            if ins_split[1][0] == '-':
                ins_1 *= -1

        if len(ins_split) > 2:
            ins_2 = int(ins_split[2][1:])
            if ins_split[2][0] == '-':
                ins_2 *= -1
        new_instruction = (ins_split[0], ins_1, ins_2)
        instructions.append(new_instruction)
    return instructions


def run_instructions(instructions, starting_regs=(0, 0)):
    reg_a, reg_b = starting_regs[0], starting_regs[1]
    next_ins = 0

    while next_ins < len(instructions):
        ins = instructions[next_ins]

        if ins[0] == 'hlf':
            if ins[1] == 'a':
                reg_a /= 2
            elif ins[1] == 'b':
                reg_b /= 2
        elif ins[0] == 'tpl':
            if ins[1] == 'a':
                reg_a *= 3
            elif ins[1] == 'b':
                reg_b *= 3
        elif ins[0] == 'inc':
            if ins[1] == 'a':
                reg_a += 1
            elif ins[1] == 'b':
                reg_b += 1
        elif ins[0] == 'jmp':
            next_ins += ins[1]
            continue
        elif ins[0] == 'jie':
            if ins[1] == 'a':
                if reg_a % 2 == 0:
                    next_ins += ins[2]
                    continue
            elif ins[1] == 'b':
                if reg_b % 2 == 0:
                    next_ins += ins[2]
                    continue
        elif ins[0] == 'jio':
            if ins[1] == 'a':
                if reg_a == 1:
                    next_ins += ins[2]
                    continue
            elif ins[1] == 'b':
                if reg_b == 1:
                    next_ins += ins[2]
                    continue

        next_ins += 1

    return (reg_a, reg_b)


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    instructions = create_instruction_list(inputs)

    output = run_instructions(instructions)

    print(f'Day 23 Puzzle 1 Solution - {output[1]}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    instructions = create_instruction_list(inputs)

    output = run_instructions(instructions, (1, 0))

    print(f'Day 23 Puzzle 2 Solution - {output[1]}')
