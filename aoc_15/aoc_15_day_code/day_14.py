"""Code to solve puzzle for day 14"""
import os

def solve():
    """Solves the day"""
    file_loc = "inputs/day14.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC15_INPUT_DAY14':
            print("Invalid input file header: Day14")
            return ''
     
        return input_file.read()
    else:
        print("Day 14 input file does not exist")
        return ''

def create_reindeer_stats(reindeer_inputs):
    """Creates a dictionary of reindeer stats for use in the race functions"""
    reindeer_stats = {}
    for reindeer in reindeer_inputs:
        reindeer_split = reindeer.split()
        reindeer_stats.setdefault(reindeer_split[0],{})
        name = reindeer_split[0]
        speed = int(reindeer_split[3])
        move_time = int(reindeer_split[6])
        rest_time = int(reindeer_split[13])
        reindeer_stats[name]["speed"] = speed
        reindeer_stats[name]["move_time"] = move_time
        reindeer_stats[name]["rest_time"] = rest_time
        reindeer_stats[name]["step_time"] = rest_time + move_time
        reindeer_stats[name]["step_dist"] = speed * move_time
    return reindeer_stats

def find_distance_moved_in_time(time, reindeer):
    """Returns the distance travelled by the reindeer in the time given"""
    steps = time // reindeer["step_time"]
    if time % reindeer["step_time"] > reindeer["move_time"]:
        steps += 1

    return steps * reindeer["step_dist"]

def step_race(reindeer_stats, race_stats):
    """Steps the race forward one second and applies points based on who is in front"""
    for r in reindeer_stats:
        if race_stats[r]['is_moving']:
            race_stats[r]['distance'] += reindeer_stats[r]['speed']
            race_stats[r]['move_time'] -= 1
            if race_stats[r]['move_time'] == 0:
                race_stats[r]['is_moving'] = False
                race_stats[r]['rest_time'] = reindeer_stats[r]['rest_time']
        else:
            race_stats[r]['rest_time'] -= 1
            if race_stats[r]['rest_time'] == 0:
                race_stats[r]['is_moving'] = True
                race_stats[r]['move_time'] = reindeer_stats[r]['move_time']

    max_distance = 0
    for r in race_stats:
        max_distance = max(race_stats[r]['distance'], max_distance)

    for r in race_stats:
        if race_stats[r]['distance'] == max_distance:
            race_stats[r]['points'] += 1

def get_max_points(race_stats):
    max_points = 0
    for r in race_stats:
        max_points = max(race_stats[r]['points'], max_points)

    return max_points

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 14 Puzzle 1 - NO INPUTS")
    else:
        reindeer_stats = create_reindeer_stats(inputs.split('\n'))

        race_time = 2503

        distances = {}

        for reindeer in reindeer_stats:
            distance = find_distance_moved_in_time(race_time, reindeer_stats[reindeer])
            distances[reindeer] = distance

        output = max(distances.values())

        print("Day 14 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 14 Puzzle 2 - NO INPUTS")
    else:
        reindeer_stats = create_reindeer_stats(inputs.split('\n'))

        race_time = 2503

        race_stats = {}

        for r in reindeer_stats:
            race_stats[r] = {
                'distance': 0,
                'points': 0,
                'rest_time': 0,
                'move_time': reindeer_stats[r]['move_time'],
                'is_moving': True
            }

        for i in range(race_time):
            step_race(reindeer_stats, race_stats)

        output = get_max_points(race_stats)

        print("Day 14 Puzzle 2 Solution - " + str(output))
    