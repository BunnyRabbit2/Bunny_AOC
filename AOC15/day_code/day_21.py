import os
import errno
import itertools

try:
    os.makedirs("output/d21/")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


def solve():
    file_loc = "inputs/day21.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split('\n')
    else:
        print("Day 21 input file does not exist")


def create_game_data(inputs):
    boss = {}
    weapons = {}
    armor = {}
    rings = {}

    for i in range(len(inputs)):
        if 'Boss' in inputs[i]:
            boss["hp"] = int(inputs[i+1].split(': ')[1])
            boss["dam"] = int(inputs[i+2].split(': ')[1])
            boss["arm"] = int(inputs[i+3].split(': ')[1])

        if 'WEAPON START' in inputs[i]:
            wC = 1
            w = inputs[i+wC]
            while not w == 'END':
                wS = w.split()
                weapons.setdefault(wS[0], {})
                weapons[wS[0]]['cost'] = int(wS[1])
                weapons[wS[0]]['dam'] = int(wS[2])
                weapons[wS[0]]['arm'] = int(wS[3])
                w = inputs[i+wC]
                wC += 1

        if 'ARMOR START' in inputs[i]:
            aC = 1
            a = inputs[i+aC]
            while not a == 'END':
                aS = a.split()
                armor.setdefault(aS[0], {})
                armor[aS[0]]['cost'] = int(aS[1])
                armor[aS[0]]['dam'] = int(aS[2])
                armor[aS[0]]['arm'] = int(aS[3])
                a = inputs[i+aC]
                aC += 1

        if 'RING START' in inputs[i]:
            rC = 1
            r = inputs[i+rC]
            while not r == 'END':
                rS = r.split()
                rings.setdefault(rS[0], {})
                rings[rS[0]]['cost'] = int(rS[1])
                rings[rS[0]]['dam'] = int(rS[2])
                rings[rS[0]]['arm'] = int(rS[3])
                r = inputs[i+rC]
                rC += 1

        armor['dummy'] = {'cost': 0, 'dam': 0, 'arm': 0}
        rings['dummy1'] = {'cost': 0, 'dam': 0, 'arm': 0}
        rings['dummy2'] = {'cost': 0, 'dam': 0, 'arm': 0}

    return (boss, weapons, armor, rings)


def fight(boss, player):
    round_num = 0
    file_out = "output/d21/output.txt"
    os.makedirs(os.path.dirname(file_out), exist_ok=True)
    if os.path.exists(file_out):
        os.remove(file_out)
    file = open(file_out, "a+")

    while boss['hp'] >= 0 and player['hp'] >= 0:
        player_dmg = max(1, player['dam'] - boss['arm'])
        boss_dmg = max(1, boss['dam'] - player['arm'])

        boss['hp'] -= player_dmg
        if boss['hp'] <= 0:
            break

        player['hp'] -= boss_dmg
        if player['hp'] <= 0:
            break

        file.write('Round ' + str(round_num) + ': Boss HP - ' +
                   str(boss['hp']) + ', Player HP - ' + str(player['hp']) + '\n')
        round_num += 1

    file.close()
    if boss['hp'] <= 0:
        return 'player'
    if player['hp'] <= 0:
        return 'boss'


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    DATA = create_game_data(inputs)
    boss = DATA[0]
    weapons = DATA[1]
    armor = DATA[2]
    rings = DATA[3]

    player = {'hp': 100, 'dam': 0, 'arm': 0}

    min_cost = 400

    for w in weapons.values():
        for a in armor.values():
            for r1, r2 in itertools.combinations(rings.values(), 2):
                player['hp'] = 100
                boss['hp'] = 104
                cost = w['cost'] + a['cost'] + r1['cost'] + r2['cost']
                player['dam'] = w['dam'] + r1['dam'] + r2['dam']
                player['arm'] = a['arm'] + r1['arm'] + r2['arm']
                if fight(boss, player) == 'player':
                    min_cost = min(cost, min_cost)

    output = min_cost

    print(f'Day 21 Puzzle 1 Solution - {output}')


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    DATA = create_game_data(inputs)
    boss = DATA[0]
    weapons = DATA[1]
    armor = DATA[2]
    rings = DATA[3]

    player = {'hp': 100, 'dam': 0, 'arm': 0}

    max_cost = 0

    for w in weapons.values():
        for a in armor.values():
            for r1, r2 in itertools.combinations(rings.values(), 2):
                player['hp'] = 100
                boss['hp'] = 104
                cost = w['cost'] + a['cost'] + r1['cost'] + r2['cost']
                player['dam'] = w['dam'] + r1['dam'] + r2['dam']
                player['arm'] = a['arm'] + r1['arm'] + r2['arm']
                if fight(boss, player) == 'boss':
                    max_cost = max(cost, max_cost)

    output = max_cost

    print(f'Day 21 Puzzle 2 Solution - {output}')
