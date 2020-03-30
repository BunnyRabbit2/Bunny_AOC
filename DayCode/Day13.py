import os
from itertools import permutations

def solve():
    fileLoc = "inputs/day13.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.readlines()
    else:
        print("Day 13 input file does not exist")

def createSeatingRules(inputs):
    names = set()
    rules = {}

    for r in inputs:
        rS = r.split()
        name1 = rS[0]
        change = rS[2]
        changeN = rS[3]
        name2 = rS[10][:-1]
        names.add(name1)
        rules.setdefault(name1,{})[name2] = ((change,changeN))

    return (names,rules)

def findHappiestTable(people, rules):
    maxHappiness = 0

    for p in permutations(people):
        happiness = 0
        for i in range(len(p)):
            if i == len(p)-1:
                p1 = p[i]
                p2 = p[0]
            else:
                p1 = p[i]
                p2 = p[i+1]
            h1 = rules[p1][p2]
            h2 = rules[p2][p1]
            if h1[0] == "lose":
                happiness -= int(h1[1])
            else:
                happiness += int(h1[1])
            if h2[0] == "lose":
                happiness -= int(h2[1])
            else:
                happiness += int(h2[1])

        maxHappiness = max(happiness,maxHappiness)

    return maxHappiness


def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    ruleSet = createSeatingRules(inputs)

    output = findHappiestTable(ruleSet[0],ruleSet[1])

    print "Day 13 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = (0,0)

    print "Day 13 Puzzle 2 Solution - " + str(output[1])