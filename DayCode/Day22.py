import os

def solve():
    fileLoc = "inputs/day22.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 22 input file does not exist")

def createGameData(inputs):
    boss = {}
    magic = {}

    for i in range(len(inputs)):
        if 'BOSS START' in inputs[i]:
            boss["hp"] = int(inputs[i+1].split(': ')[1])
            boss["dam"] = int(inputs[i+2].split(': ')[1])

        if 'MAGIC START' in inputs[i]:
            mC = 1
            m = inputs[i+mC]
            while not m == 'END':
                mS = m.split()
                magic.setdefault(mS[0],{})
                magic[mS[0]]['cost'] = int(mS[1])
                
                m = inputs[i+mC]
                mC += 1

    return (boss,magic)

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
    
    output = 0

    print "Day 22 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    DATA = createGameData(inputs)
    boss = DATA[0]

    output = 0

    print "Day 22 Puzzle 2 Solution - " + str(output)