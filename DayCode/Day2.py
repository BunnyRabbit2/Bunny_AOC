import os

def solve():
    fileLoc = "inputs/day2.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split()
    else:
        print("Day 2 input file does not exist")

def calculateWrapping(l,w,h):
    side1 = l*w
    side2 = l*h
    side3 = w*h

    smallestSide = min(side1,side2,side3)

    surfaceArea = 2*side1 + 2*side2 + 2*side3

    return surfaceArea + smallestSide

def getLwhFromString(stringLwh):
    values = stringLwh.split('x')
    l = int(values[0])
    w = int(values[1])
    h = int(values[2])

    return (l,w,h)

def calculateTotalSF(inputs):
    totalSF = 0

    for s in inputs:
        values = getLwhFromString(s)
        totalSF += calculateWrapping(values[0],values[1],values[2])

    return (totalSF,0)

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    output = calculateTotalSF(inputs)

    print "Day 2 Puzzle 1 Solution - " + str(output[0])

def solvePuzzle2(fileLocation):
    output = (0,0)

    print "Day 2 Puzzle 2 Solution - " + str(output[1])