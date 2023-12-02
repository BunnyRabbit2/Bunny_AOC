import os


def solve():
    file_loc = "inputs/day5.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split()
    else:
        print("Day 5 input file does not exist")


def check_string_is_nice(test_string):
    has_pair = False
    naughty_pairs = ["ab", "cd", "pq", "xy"]
    vowels = []
    vowel_check = ["a", "e", "i", "o", "u"]

    for i in range(len(test_string)):
        pair_check = test_string[i:i+2]
        if pair_check in naughty_pairs:
            return False

        if len(pair_check) > 1:
            if pair_check[0] == pair_check[1]:
                has_pair = True

        char = test_string[i]

        if char in vowel_check:
            vowels.append(char)

    if has_pair and len(vowels) >= 3:
        return True
    else:
        return False


def check_string_is_nice_alt(test_string):
    has_repeat_pair = False
    has_triple_set = False

    for i in range(len(test_string)):
        test_pair = test_string[i:i+2]
        if len(test_pair) > 1:
            new_test_string = test_string
            new_test_string = new_test_string[:i] + \
                "--" + new_test_string[i + 2:]

            for j in range(len(test_string)):
                new_test_pair = new_test_string[j:j+2]
                if new_test_pair == test_pair:
                    has_repeat_pair = True

        check_triple = test_string[i:i+3]
        if len(check_triple) > 2:
            if check_triple[0] == check_triple[2] and check_triple[0] != check_triple[1]:
                has_triple_set = True

    if has_triple_set and has_repeat_pair:
        return True
    else:
        return False


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)
    niceStrings = 0

    for s in inputs:
        if check_string_is_nice(s):
            niceStrings += 1

    print(f'Day 5 Puzzle 1 Solution - {niceStrings}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)
    niceStrings = 0

    for s in inputs:
        if check_string_is_nice_alt(s):
            niceStrings += 1

    print(f'Day 5 Puzzle 2 Solution - {niceStrings}')
