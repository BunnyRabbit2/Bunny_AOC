import os
import re

def solve():
    file_loc = "inputs/day02.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC23_INPUT_DAY02':
            print("Invalid input file header: Day02")
            return False
     
        return file.read()
    else:
        print("Day 02 input file does not exist")

def create_game_data(input_lines: list[str]):
    # Game 1: 4 red, 18 green, 15 blue; 17 green, 18 blue, 9 red; 8 red, 14 green, 6 blue; 14 green, 12 blue, 2 red
    red_fetch = re.compile(r'(\d*) red')
    green_fetch = re.compile(r'(\d*) green')
    blue_fetch = re.compile(r'(\d*) blue')

    game_list = {}
    for line in input_lines:
        line_split = line.split(':')
        game_num = int(line_split[0].split(' ')[-1])
        game_list[game_num] = {
            'game_rounds': [],
            'min_red': 0,
            'min_green': 0,
            'min_blue': 0,
            'power': 0
        }

        game_rounds = line_split[1].split(';')

        for game_round in game_rounds:
            round_stats = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            red_search = red_fetch.findall(game_round)
            if len(red_search) > 0: round_stats['red'] = int(red_search[0])
            game_list[game_num]['min_red'] = max(game_list[game_num]['min_red'], round_stats['red'])

            green_search = green_fetch.findall(game_round)
            if len(green_search) > 0: round_stats['green'] = int(green_search[0])
            game_list[game_num]['min_green'] = max(game_list[game_num]['min_green'], round_stats['green'])

            blue_search = blue_fetch.findall(game_round)
            if len(blue_search) > 0: round_stats['blue'] = int(blue_search[0])
            game_list[game_num]['min_blue'] = max(game_list[game_num]['min_blue'], round_stats['blue'])

            game_list[game_num]['game_rounds'].append(round_stats)

        game_list[game_num]['power'] = game_list[game_num]['min_red'] * game_list[game_num]['min_green'] * game_list[game_num]['min_blue']

    return game_list

def get_correct_games(red_num: int, green_num: int, blue_num: int, games_data: dict):
    correct_game_ids = []

    for game_id, game_data in games_data.items():
        correct_game = True
        for game_round in game_data['game_rounds']:
            if game_round['red'] > red_num or game_round['green'] > green_num or game_round['blue'] > blue_num:
                correct_game = False
        if correct_game: correct_game_ids.append(game_id)
    
    return correct_game_ids

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return
    
    game_data = create_game_data(inputs.split('\n'))

    correct_game_ids = get_correct_games(12, 13, 14, game_data)

    output = sum(correct_game_ids)

    print(f'Day 02 Puzzle 1 Solution - {output}')

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    game_data = create_game_data(inputs.split('\n'))

    output = sum([game_data[game]['power'] for game in game_data])

    print(f'Day_02 Puzzle 2 Solution - {output}')
    