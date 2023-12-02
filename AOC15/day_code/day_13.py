import os
from itertools import permutations


def solve():
    file_loc = "inputs/day13.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.readlines()
    else:
        print("Day 13 input file does not exist")


def create_seating_rules(inputs):
    names = set()
    rules = {}

    for rule in inputs:
        rule_split = rule.split()
        name_1 = rule_split[0]
        change = rule_split[2]
        change_name = rule_split[3]
        name_2 = rule_split[10][:-1]
        names.add(name_1)
        rules.setdefault(name_1, {})[name_2] = ((change, change_name))

    return (names, rules)


def find_happiest_table(people, rules):
    max_happiness = 0

    for p in permutations(people):
        happiness = 0
        for i in range(len(p)):
            if i == len(p)-1:
                p1 = p[i]
                p2 = p[0]
            else:
                p1 = p[i]
                p2 = p[i+1]
            h1 = rules[p1][p2]
            h2 = rules[p2][p1]
            if h1[0] == "lose":
                happiness -= int(h1[1])
            else:
                happiness += int(h1[1])
            if h2[0] == "lose":
                happiness -= int(h2[1])
            else:
                happiness += int(h2[1])

        max_happiness = max(happiness, max_happiness)

    return max_happiness


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    rule_set = create_seating_rules(inputs)

    output = find_happiest_table(rule_set[0], rule_set[1])

    print(f'Day 13 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    rule_set = create_seating_rules(inputs)

    myself = "Myself"

    for p in rule_set[0]:
        rule_set[1].setdefault(myself, {})[p] = (("gain", 0))
        rule_set[1].setdefault(p, {})[myself] = (("gain", 0))

    rule_set[0].add(myself)

    output = find_happiest_table(rule_set[0], rule_set[1])

    print(f'Day 13 Puzzle 2 Solution - {output}')
