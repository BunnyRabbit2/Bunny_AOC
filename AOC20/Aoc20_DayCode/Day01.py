import os

def solve():
    fileLoc = "inputs/day01.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        f = file.readline().strip()
        if not f == 'AOC20_INPUT_DAY01':
            print "Invalid input file header: Day01"
            return False
     
        lines = file.readlines()
        n = []
        for l in lines:
            n.append(int(l))
        return n
    else:
        print "Day 01 input file does not exist"

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    for i in range(len(inputs)):
        for j in range(len(inputs)):
            if i == j:
                continue

            a = inputs[i]
            b = inputs[j]

            if a + b == 2020:
                output = a * b

    print "Day 01 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    print "Day 01 Puzzle 2 Solution - " + str(output)
    