import os
import operator


def solve():
    file_loc = "inputs/day14.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.readlines()
    else:
        print("Day 14 input file does not exist")


def create_reindeer_stats(inputs):
    reindeer = {}
    for line in inputs:
        reindeer_split = line.split()
        reindeer.setdefault(reindeer_split[0], {})
        name = reindeer_split[0]
        speed = int(reindeer_split[3])
        time = int(reindeer_split[6])
        rest = int(reindeer_split[13])
        reindeer[name]["speed"] = speed
        reindeer[name]["time"] = time
        reindeer[name]["rest"] = rest
        reindeer[name]["step_time"] = rest + time
        reindeer[name]["step_dist"] = speed * time
    return reindeer


def find_distance_in_time(time, r):
    steps = time / r["step_time"]
    if time % r["step_time"] > r["time"]:
        steps += 1

    return steps * r["step_dist"]


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    rs = create_reindeer_stats(inputs)

    raceTime = 2503

    distances = {}

    for r in rs:
        d = find_distance_in_time(raceTime, rs[r])
        distances[r] = d

    output = max(distances.items(), key=operator.itemgetter(1))

    print(f'Day 14 Puzzle 1 Solution - {output[1]}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    rs = create_reindeer_stats(inputs)

    raceTime = 2503

    scores = {}
    for r in rs:
        scores[r] = [True, 0, 0, 0]  # flying, score, distance, time

    for i in range(raceTime):
        for r in rs:
            if scores[r][0]:
                s = rs[r]["speed"]
                scores[r][2] += s
                scores[r][3] += 1
                if scores[r][3] >= rs[r]["time"]:
                    scores[r][0] = False
                    scores[r][3] = 0
            else:
                scores[r][3] += 1
                if scores[r][3] >= rs[r]["rest"]:
                    scores[r][0] = True
                    scores[r][3] = 0

        lead = scores[next(iter(scores))]

        for s in scores:
            if scores[s][2] > lead[2]:
                lead = scores[s]

        lead_reindeers = []
        ld = lead[2]
        for s in scores:
            cd = scores[s][2]
            if ld == cd:
                # if scores[s][2] = lead[1][2]:
                lead_reindeers.append(s)

        for r in lead_reindeers:
            scores[r][1] += 1

    output = scores[next(iter(scores))]

    for s in scores:
        if scores[s][1] > output[1]:
            output = scores[s]

    print(f'Day 14 Puzzle 2 Solution - {output[1]}')
