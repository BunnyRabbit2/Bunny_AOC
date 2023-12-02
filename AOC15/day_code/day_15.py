import os


def solve():
    file_loc = "inputs/day15.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split("\n")
    else:
        print("Day 15 input file does not exist")


def create_ingredients(inputs):
    ingredients = []

    for line in inputs:
        values = line.split(": ")[1].split(", ")
        vA = []

        for v in values:
            vA.append(int(v.split()[1]))

        ingredients.append(vA)

    return ingredients


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)
    ings = create_ingredients(inputs)
    t = [[2, 0, -2, 0, 3], [0, 5, -3, 0, 3],
         [0, 0, 5, -1, 8], [0, -1, 0, 5, 8]]

    score = 0
    max_score = 0

    for i in range(0, 100):
        for j in range(0, 100-i):
            for k in range(0, 100-i-j):
                h = 100-i-j-k

                if h == 0:
                    continue

                cap = max(0, ings[0][0]*i+ings[1][0] *
                          j+ings[2][0]*k+ings[3][0]*h)
                dur = max(0, ings[0][1]*i+ings[1][1] *
                          j+ings[2][1]*k+ings[3][1]*h)
                fla = max(0, ings[0][2]*i+ings[1][2] *
                          j+ings[2][2]*k+ings[3][2]*h)
                tex = max(0, ings[0][3]*i+ings[1][3] *
                          j+ings[2][3]*k+ings[3][3]*h)
                cal = max(0, ings[0][4]*i+ings[1][4] *
                          j+ings[2][4]*k+ings[3][4]*h)

                score = cap * dur * fla * tex

                max_score = max(score, max_score)

    print(f'Day 15 Puzzle 1 Solution - {max_score}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)
    ings = create_ingredients(inputs)
    t = [[2, 0, -2, 0, 3], [0, 5, -3, 0, 3],
         [0, 0, 5, -1, 8], [0, -1, 0, 5, 8]]

    score = 0
    max_score = 0

    for i in range(0, 100):
        for j in range(0, 100-i):
            for k in range(0, 100-i-j):
                h = 100-i-j-k

                if h == 0:
                    continue

                cap = max(0, ings[0][0]*i+ings[1][0] *
                          j+ings[2][0]*k+ings[3][0]*h)
                dur = max(0, ings[0][1]*i+ings[1][1] *
                          j+ings[2][1]*k+ings[3][1]*h)
                fla = max(0, ings[0][2]*i+ings[1][2] *
                          j+ings[2][2]*k+ings[3][2]*h)
                tex = max(0, ings[0][3]*i+ings[1][3] *
                          j+ings[2][3]*k+ings[3][3]*h)
                cal = max(0, ings[0][4]*i+ings[1][4] *
                          j+ings[2][4]*k+ings[3][4]*h)

                score = cap * dur * fla * tex

                if not cal == 500:
                    continue

                max_score = max(score, max_score)

    print(f'Day 15 Puzzle 1 Solution - {max_score}')
