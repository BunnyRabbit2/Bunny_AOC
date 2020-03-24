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

def processInputs(inputs):
    currentFloor = 0
    enteredBasement = False
    firstEnteredBasement = 1

    for c in inputs:
        if c == '(':
            currentFloor += 1
        elif c == ')':
            currentFloor -= 1
        if not enteredBasement:
            if currentFloor < 0:
                enteredBasement = True
            else:
                firstEnteredBasement += 1

    return (currentFloor,firstEnteredBasement)

def solvePuzzle1(fileLocation):
    output = processInputs(loadInputs(fileLocation))    

    print "Day 1 Puzzle 1 Solution - " + str(output[0])

def solvePuzzle2(fileLocation):
    output = processInputs(loadInputs(fileLocation)) 

    print "Day 1 Puzzle 2 Solution - " + str(output[1])