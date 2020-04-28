import os, re

def solve():
    fileLoc = "inputs/day19.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split('\n')
    else:
        print("Day 19 input file does not exist")

def createSubstitutions(inputs):
    newSubs = []
    mol = ""

    for l in inputs:
        ls = l.split()
        if len(ls) < 2:
            continue

        newSubs.append((ls[0],ls[2]))

    mol = inputs[-1]

    return (newSubs,mol)
        

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    t = createSubstitutions(inputs)

    subs = t[0]
    mol = t[1]
    uniqueMs = set()

    for s in subs:
        indexes = [m.start() for m in re.finditer(s[0], mol)]

        for i in range(len(indexes)):
            reS = '^(.*?(' + s[0] + '.*?){' + str(i) + '})' + s[0] + ''
            newM = re.sub(reS, '\\1' + s[1], mol)
            uniqueMs.add(newM)

    output = len(uniqueMs)

    print "Day 19 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    mol = createSubstitutions(inputs)[1]

    RnN = [m.start() for m in re.finditer('Rn', mol)]
    ArN = [m.start() for m in re.finditer('Ar', mol)]
    YsN = [m.start() for m in re.finditer('Y', mol)]
    nEl = [m.start() for m in re.finditer('[A-Z]', mol)]

    output = len(nEl) - len(RnN) - len(ArN) - (2*len(YsN)) - 1

    print "Day 19 Puzzle 2 Solution - " + str(output)