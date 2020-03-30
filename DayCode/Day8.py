import os
import re

def solve():
    fileLoc = "inputs/day8.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split()
    else:
        print("Day 8 input file does not exist")

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    charCount = 0
    memCount = 0

    for s in inputs:
        charCount += len(s)
        memCount += len(eval(s))

    output = charCount - memCount

    print "Day 8 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    charCount = 0
    newCharCount = 0

    for s in inputs:
        charCount += len(s)
        newCharCount += len(re.escape(s)) + 2

    output = newCharCount - charCount

    print "Day 8 Puzzle 2 Solution - " + str(output)