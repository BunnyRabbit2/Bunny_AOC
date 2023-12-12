import os
from pprint import pformat


def solve():
    file_loc = "inputs/day07.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC23_INPUT_DAY07':
            print("Invalid input file header: Day07")
            return False

        return file.read()
    else:
        print("Day 07 input file does not exist")


def check_hand_for_type(hand_data, use_joker_rule=False):
    sorted_hand = sorted(hand_data)

    check_groups = list({tuple(i for i in sorted_hand if i == x)
                         for x in sorted_hand})

    check_groups = sorted(check_groups, key=lambda l: (len(l), l))[::-1]

    if use_joker_rule and 1 in hand_data:
        b = True
        most_common_non_j = None

        for i in range(len(check_groups)):
            if check_groups[i][0] != 1:
                most_common_non_j = check_groups[i][0]
                break
        
        if most_common_non_j is None: most_common_non_j = 1

        sorted_hand = sorted([most_common_non_j if v == 1 else v for v in sorted_hand])

        check_groups = {tuple(i for i in sorted_hand if i == x)
                        for x in sorted_hand}

        check_groups = sorted(check_groups, key=lambda l: (len(l), l))[::-1]

    if use_joker_rule and 1 in hand_data:
        b = False

    hand_type = 'high-card'

    if len(check_groups) == 1:
        # return 'five-of-a-kind'
        hand_type = 'five-of-a-kind'

    if len(check_groups) == 2:
        if len(check_groups[0]) == 4:
            # return 'four-of-a-kind'
            hand_type = 'four-of-a-kind'
        else:
            # return 'full-house'
            hand_type = 'full-house'

    if len(check_groups) == 3:
        if (len(check_groups[0]) == 3):
            # return 'three-of-a-kind'
            hand_type = 'three-of-a-kind'
        else:
            # return 'two-pair'
            hand_type = 'two-pair'

    if len(check_groups) == 4:
        # return 'one-pair'
        hand_type = 'one-pair'

    # return 'high-card'
    if use_joker_rule and 1 in hand_data:
        b = True
    return hand_type


def gen_hand_buckets(input_lines, use_joker_rule=False):
    replace_dict = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    if use_joker_rule:
        replace_dict['J'] = 1

    hand_buckets = {
        'five-of-a-kind': {},
        'four-of-a-kind': {},
        'full-house': {},
        'three-of-a-kind': {},
        'two-pair': {},
        'one-pair': {},
        'high-card': {}
    }

    for input_line in input_lines:
        line_split = input_line.split()
        hand = tuple(replace_dict[c] for c in line_split[0])

        hand_buckets[check_hand_for_type(hand, use_joker_rule)][hand] = (
            line_split[0], int(line_split[1]))

    for hand_bucket in hand_buckets:
        hand_buckets[hand_bucket]['sorted_keys'] = sorted(
            hand_buckets[hand_bucket].keys(), key=lambda x: (x[0], x[1], x[2], x[3], x[4]))

    hand_buckets['winning-order'] = [
        'five-of-a-kind', 'four-of-a-kind', 'full-house', 'three-of-a-kind', 'two-pair', 'one-pair', 'high-card'
    ]

    return hand_buckets


def gen_full_hand_list(hand_buckets):
    full_hand_list = []

    for bucket in hand_buckets['winning-order'][::-1]:
        sorted_keys = hand_buckets[bucket]['sorted_keys']
        full_hand_list.extend([(k, hand_buckets[bucket][k])
                              for k in sorted_keys])

    return full_hand_list


def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    hand_buckets = gen_hand_buckets(inputs.splitlines())

    full_hand_list = gen_full_hand_list(hand_buckets)

    winnings = [(x + 1) * v[1][1] for x, v in enumerate(full_hand_list)]

    debug_file = '''
    with open('private/test_output_d07p01.txt', 'w+') as out_file:
        out_hand_list = [(v[0], v[1], x + 1, (x + 1) * v[1][1]) for x, v in enumerate(full_hand_list)]
        out_file.write(pformat(out_hand_list))
        out_file.write(f'\n\n{sum(winnings)}')
    '''

    output = sum(winnings)

    print(f'Day 07 Puzzle 1 Solution - {output}')

    if output != 248113761:
        print("Failing puzzle 1")


def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    hand_buckets = gen_hand_buckets(inputs.splitlines(), True)

    full_hand_list = gen_full_hand_list(hand_buckets)

    winnings = [(x + 1) * v[1][1] for x, v in enumerate(full_hand_list)]

    with open('private/test_output_d07p02.txt', 'w+') as out_file:
        out_hand_list = [(v[0], v[1], x + 1, (x + 1) * v[1][1]) for x, v in enumerate(full_hand_list)]
        out_file.write(pformat(out_hand_list))
        out_file.write(f'\n\n{sum(winnings)}')

    output = sum(winnings)

    print(f'Day_07 Puzzle 2 Solution - {output}')
