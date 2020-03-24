import os

def solve():
    fileLoc = "inputs/day1.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 1 input file does not exist")

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    currentFloor = 0

    for c in inputs:
        if c == '(':
            currentFloor += 1
        elif c == ')':
            currentFloor -= 1

    print "Day 1 Puzle 1 Solution - " + str(currentFloor)

def solvePuzzle2(fileLocation):
    

    print "Day 1 Puzle 2 Solution - " + " "