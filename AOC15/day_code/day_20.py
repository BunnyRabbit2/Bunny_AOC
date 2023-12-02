import os


def solve():
    file_loc = "inputs/day20.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read()
    else:
        print("Day 20 input file does not exist")


def solve_puzzle_1(file_location):
    inputs = int(load_inputs(file_location))

    house_num = 1000000

    output = 0

    houses = []
    for i in range(house_num):
        houses.append(0)

    for i in range(1, len(houses)):
        for j in range(i, len(houses), i):
            houses[j] += i * 10

    for i in range(1, len(houses)):
        if houses[i] >= inputs:
            output = i
            break

    print(f'Day 20 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    inputs = int(load_inputs(file_location))

    house_num = 1000000

    output = 0

    houses = []
    for i in range(house_num):
        houses.append(0)

    for i in range(1, len(houses)):
        house_count = 0
        for j in range(i, len(houses), i):
            houses[j] += i * 11
            house_count += 1
            if house_count >= 50:
                break

    for i in range(1, len(houses)):
        if houses[i] >= inputs:
            output = i
            break

    print(f'Day 20 Puzzle 2 Solution - {output}')
