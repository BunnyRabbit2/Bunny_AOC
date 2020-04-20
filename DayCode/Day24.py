import os

def solve():
    fileLoc = "inputs/day24.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 24 input file does not exist")

def solvePuzzle1(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = 0

    print "Day 24 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = 0

    print "Day 24 Puzzle 2 Solution - " + str(output)