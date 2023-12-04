import os
import re

def solve():
    file_loc = "inputs/day04.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC23_INPUT_DAY04':
            print("Invalid input file header: Day04")
            return False
     
        return file.read()
    else:
        print("Day 04 input file does not exist")

def create_card_data(input_lines: list[str]):
    card_number_grabber = re.compile(r'(\d+):')
    number_grabber = re.compile(r'\s*(\d+)\s*')

    card_data = {}
    for line in input_lines:
        card_number = int(card_number_grabber.findall(line)[0])

        line_split = line.split(':')
        number_split = line_split[1].split('|')
        
        winning_numbers = [int(v) for v in number_grabber.findall(number_split[0])]
        numbers_to_check = [int(v) for v in number_grabber.findall(number_split[1])]

        numbers_that_win = [v for v in numbers_to_check if v in winning_numbers]

        if len(numbers_that_win) > 0:
            card_points = 1 * 2**(len(numbers_that_win) - 1) # Offset for first number
        else:
            card_points = 0

        card_data[card_number] = {
            'winning_numbers': winning_numbers,
            'numbers_to_check': numbers_to_check,
            'numbers_that_win': numbers_that_win,
            'card_points': card_points
        }

    return card_data

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return
    
    card_data = create_card_data(inputs.split('\n'))

    output = sum([card_data[card]['card_points'] for card in card_data])

    print(f'Day 04 Puzzle 1 Solution - {output}')

def create_card_counts(card_num: int, card_counts: dict, card_data: dict):
    if card_num in card_counts:
        card_counts[card_num] += 1
    else:
        return
    
    numbers_that_win = card_data[card_num]['numbers_that_win']

    for i in range(1, len(numbers_that_win) + 1):
        create_card_counts(card_num + i, card_counts, card_data)

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    test_input = [
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
    ]

    card_data = create_card_data(test_input)

    card_data = create_card_data(inputs.split('\n'))

    card_counts = {card_num: 0 for card_num in card_data}

    for card_num in card_data:
        create_card_counts(card_num, card_counts, card_data)

    output = sum(card_counts.values())

    print(f'Day_04 Puzzle 2 Solution - {output}')
    