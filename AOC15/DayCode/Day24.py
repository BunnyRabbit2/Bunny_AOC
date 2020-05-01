import os
from itertools import combinations
from operator import mul

def solve():
    fileLoc = "inputs/day24.txt"
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
        print("Day 24 input file does not exist")

def hasWeight(packages,sub,weight,parts):
    for i in range(1,len(packages)):
        for s in (c for c in combinations(packages,i) if sum(c) == weight):
            if sub == 2:
                return True
            elif sub < parts:
                return hasWeight(list(set(packages) - set(s)), sub-1,weight,parts)
            elif hasWeight(list(set(packages) - set(s)), sub-1,weight,parts):
                return reduce(mul,s,1)

def solvePuzzle1(fileLocation):
    packages = loadInputs(fileLocation)

    parts = 3    
    output = hasWeight(packages,parts,sum(packages) // parts,parts)

    print "Day 24 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    packages = loadInputs(fileLocation)

    parts = 4    
    output = hasWeight(packages,parts,sum(packages) // parts,parts)

    print "Day 24 Puzzle 2 Solution - " + str(output)