import os
import re


def solve():
    file_loc = "inputs/day19.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split('\n')
    else:
        print("Day 19 input file does not exist")


def create_substitutions(inputs):
    new_subs = []
    mol = ""

    for l in inputs:
        ls = l.split()
        if len(ls) < 2:
            continue

        new_subs.append((ls[0], ls[2]))

    mol = inputs[-1]

    return (new_subs, mol)


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    t = create_substitutions(inputs)

    subs = t[0]
    mol = t[1]
    unique_ms = set()

    for s in subs:
        indexes = [m.start() for m in re.finditer(s[0], mol)]

        for i in range(len(indexes)):
            re_search = '^(.*?(' + s[0] + '.*?){' + str(i) + '})' + s[0] + ''
            new_m = re.sub(re_search, '\\1' + s[1], mol)
            unique_ms.add(new_m)

    output = len(unique_ms)

    print(f'Day 19 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    mol = create_substitutions(inputs)[1]

    RnN = [m.start() for m in re.finditer('Rn', mol)]
    ArN = [m.start() for m in re.finditer('Ar', mol)]
    YsN = [m.start() for m in re.finditer('Y', mol)]
    nEl = [m.start() for m in re.finditer('[A-Z]', mol)]

    output = len(nEl) - len(RnN) - len(ArN) - (2*len(YsN)) - 1

    print(f'Day 19 Puzzle 2 Solution - {output}')
