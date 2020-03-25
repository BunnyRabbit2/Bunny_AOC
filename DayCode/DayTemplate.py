import os

def solve():
    fileLoc = "inputs/day*.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split()
    else:
        print("Day * input file does not exist")

def solvePuzzle1(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = (0,0)

    print "Day * Puzzle 1 Solution - " + str(output[0])

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = (0,0)

    print "Day * Puzzle 2 Solution - " + str(output[1])