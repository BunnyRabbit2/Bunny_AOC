import os
import itertools

def solve():
    fileLoc = "inputs/day17.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        lines = file.readlines()
        n = []
        for l in lines:
            n.append(int(l))
        return n
    else:
        print("Day 17 input file does not exist")

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    output = 0

    for i in range(len(inputs)):
        sub = 0
        for comb in itertools.combinations(inputs,i):
            if sum(comb) == 150:
                sub += 1
        output += sub

    print "Day 17 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    output = 0
    minContainers = 0

    for i in range(len(inputs)):
        sub = 0
        for comb in itertools.combinations(inputs,i):
            if sum(comb) == 150:
                minContainers = i
                sub += 1
        output += sub
        if minContainers > 0:
            break

    print "Day 17 Puzzle 2 Solution - " + str(output)