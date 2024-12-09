"""Code to solve puzzle for day 13"""
import os
from itertools import permutations


def solve():
    """Solves the day"""
    file_loc = "inputs/day13.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY13':
            print("Invalid input file header: Day13")
            return ''

        return input_file.read()
    else:
        print("Day 13 input file does not exist")
        return ''


def create_seating_rules(inputs):
    """Creates the name and rules list to work out happiest tables"""
    names = set()
    rules = {}

    for rule in inputs:
        rule_split = rule.split()
        name_1 = rule_split[0]
        change_type = rule_split[2]
        change_value = rule_split[3]
        name_2 = rule_split[10][:-1]
        names.add(name_1)
        rules.setdefault(name_1, {})[name_2] = ((change_type, change_value))

    return (names, rules)


def find_happiest_table(people, rules):
    """Checks all given people and rules for the happiest seating arrangement"""
    max_happiness = 0

    for perm in permutations(people):
        happiness = 0
        for i in range(len(perm)):
            if i == len(perm)-1:
                perm_1 = perm[i]
                perm_2 = perm[0]
            else:
                perm_1 = perm[i]
                perm_2 = perm[i+1]
            happiness_change_1 = rules[perm_1][perm_2]
            happiness_change_2 = rules[perm_2][perm_1]
            if happiness_change_1[0] == "lose":
                happiness -= int(happiness_change_1[1])
            else:
                happiness += int(happiness_change_1[1])
            if happiness_change_2[0] == "lose":
                happiness -= int(happiness_change_2[1])
            else:
                happiness += int(happiness_change_2[1])

        max_happiness = max(happiness, max_happiness)

    return max_happiness


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 13 Puzzle 1 - NO INPUTS")
    else:
        people, rules = create_seating_rules(inputs.split('\n'))

        output = find_happiest_table(people, rules)

        print("Day 13 Puzzle 1 Solution - " + str(output))


def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 13 Puzzle 2 - NO INPUTS")
    else:
        people, rules = create_seating_rules(inputs.split('\n'))

        myself_name = "Myself"

        for person in people:
            rules.setdefault(myself_name, {})[person] = (("gain", 0))
            rules.setdefault(person, {})[myself_name] = (("gain", 0))

        people.add(myself_name)

        output = find_happiest_table(people, rules)

        print("Day 13 Puzzle 2 Solution - " + str(output))
