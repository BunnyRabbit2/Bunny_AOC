import os

def solve():
    fileLoc = "inputs/day2.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 2 input file does not exist")

def solvePuzzle1(fileLocation):
    output = (0,0)   

    print "Day 2 Puzzle 1 Solution - " + str(output[0])

def solvePuzzle2(fileLocation):
    output = (0,0)

    print "Day 2 Puzzle 2 Solution - " + str(output[1])