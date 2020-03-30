import os
import re

def solve():
    fileLoc = "inputs/day10.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 10 input file does not exist")

def lookAndSay(s):
    re_d = re.compile(r'((\d)\2*)')

    def replace(match_obj):
        s = match_obj.group(1)
        return str(len(s)) + s[0]

    return re_d.sub(replace,s)

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    for i in range(40):
        inputs = lookAndSay(inputs)

    output = len(inputs)

    print "Day 10 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    for i in range(50):
        inputs = lookAndSay(inputs)

    output = len(inputs)

    print "Day 10 Puzzle 2 Solution - " + str(output)