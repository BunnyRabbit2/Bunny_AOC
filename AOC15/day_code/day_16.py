import os


def solve():
    file_loc = "inputs/day16.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split('\n')
    else:
        print("Day 16 input file does not exist")


def create_sues(inputs):
    sues = []

    def is_a_dog(d):
        return d == "samoyeds" or d == "pomeranians" or d == "akitas" or d == "vizalas"

    for sue in inputs:
        sA = sue.replace(":", "").replace(",", "")
        sA = sA.split()
        sue = {
            "children": 0,
            "cats": 0,
            "samoyeds": 0,
            "pomeranians": 0,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 0,
            "trees": 0,
            "cars": 0,
            "perfumes": 0
        }
        sue[sA[2]] = int(sA[3])
        sue[sA[4]] = int(sA[5])
        sue[sA[6]] = int(sA[7])

        sues.append(sue)

    return sues


def find_number_sue(sues, check_sue):
    sue_num = 0
    possible_sues = []

    for i in range(len(sues)):
        sue = sues[i]

        match_count = 0

        for sue_key in sue:
            if sue[sue_key] == check_sue[sue_key]:
                match_count += 1

        if match_count > 4:
            possible_sues.append((sue, match_count))
            sue_num = i

    return sue_num


def find_number_sue_alt(sues, check_sue):
    sue_num = 0
    possible_sues = []

    for i in range(len(sues)):
        sue = sues[i]

        match_count = 0

        for sue_key in sue:
            if sue_key == "cats" or sue_key == "trees":
                if sue[sue_key] > check_sue[sue_key]:
                    match_count += 1
            elif sue_key == "pomeranians" or sue_key == "goldfish":
                if sue[sue_key] < check_sue[sue_key]:
                    match_count += 1
            elif sue[sue_key] == check_sue[sue_key]:
                match_count += 1

        if match_count > 6:
            possible_sues.append((sue, match_count))
            sue_num = i

    return sue_num


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    sues = create_sues(inputs)

    check_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    output = find_number_sue(sues, check_sue)

    print(f'Day 16 Puzzle 1 Solution - {output + 1}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    sues = create_sues(inputs)

    check_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    output = find_number_sue_alt(sues, check_sue)

    print(f'Day 16 Puzzle 1 Solution - {output + 1}')
