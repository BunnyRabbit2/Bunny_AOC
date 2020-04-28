import os, errno
import itertools

try:
    os.makedirs("output/d21/")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

def solve():
    fileLoc = "inputs/day21.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split('\n')
    else:
        print("Day 21 input file does not exist")

def createGameData(inputs):
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
                weapons.setdefault(wS[0],{})
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
                armor.setdefault(aS[0],{})
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
                rings.setdefault(rS[0],{})
                rings[rS[0]]['cost'] = int(rS[1])
                rings[rS[0]]['dam'] = int(rS[2])
                rings[rS[0]]['arm'] = int(rS[3])
                r = inputs[i+rC]
                rC += 1

        armor['dummy'] = {'cost':0, 'dam':0, 'arm':0}
        rings['dummy1'] = {'cost':0, 'dam':0, 'arm':0}
        rings['dummy2'] = {'cost':0, 'dam':0, 'arm':0}

    return (boss,weapons,armor,rings)

def fight(boss,player):
    roundN = 0
    fileP = "output/d21/output.txt"
    os.remove(fileP)
    file = open(fileP, "a+")

    while boss['hp'] >= 0 and player['hp'] >= 0:
        playerDam = max(1,player['dam'] - boss['arm'])
        bossDam = max(1,boss['dam'] - player['arm'])

        boss['hp'] -= playerDam
        if boss['hp'] <= 0:
            break

        player['hp'] -= bossDam
        if player['hp'] <= 0:
            break

        file.write('Round ' + str(roundN) + ': Boss HP - ' + str(boss['hp']) + ', Player HP - ' + str(player['hp']) + '\n')
        roundN += 1

    file.close()
    if boss['hp'] <= 0:
        return 'player'
    if player['hp'] <= 0:
        return 'boss'

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    DATA = createGameData(inputs)
    boss = DATA[0]
    weapons = DATA[1]
    armor = DATA[2]
    rings = DATA[3]

    player = {'hp': 100,'dam': 0,'arm': 0}

    minCost = 400

    for w in weapons.values():
        for a in armor.values():
            for r1, r2 in itertools.combinations(rings.values(),2):
                player['hp'] = 100
                boss['hp'] = 104
                cost = w['cost'] + a['cost'] + r1['cost'] + r2['cost']
                player['dam'] = w['dam'] + r1['dam'] + r2['dam']
                player['arm'] = a['arm'] + r1['arm'] + r2['arm']
                if fight(boss,player) == 'player':
                    minCost = min(cost,minCost)

    output = minCost

    print "Day 21 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    DATA = createGameData(inputs)
    boss = DATA[0]
    weapons = DATA[1]
    armor = DATA[2]
    rings = DATA[3]

    player = {'hp': 100,'dam': 0,'arm': 0}

    maxCost = 0

    for w in weapons.values():
        for a in armor.values():
            for r1, r2 in itertools.combinations(rings.values(),2):
                player['hp'] = 100
                boss['hp'] = 104
                cost = w['cost'] + a['cost'] + r1['cost'] + r2['cost']
                player['dam'] = w['dam'] + r1['dam'] + r2['dam']
                player['arm'] = a['arm'] + r1['arm'] + r2['arm']
                if fight(boss,player) == 'boss':
                    maxCost = max(cost,maxCost)

    output = maxCost

    print "Day 21 Puzzle 2 Solution - " + str(output)