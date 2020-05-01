import os, re

def solve():
    fileLoc = "inputs/day25.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        nums = [int(s) for s in re.findall(r'\b\d+\b', file.read())]
        return nums
    else:
        print("Day 25 input file does not exist")

def generateCodeField(width,height):
    x,y = 0,0
    value = 20151125
    grid = []

    for y in range(height):
        grid.append([])
        for x in range(width):
            grid[y].append(0)

    def nextI(i):
        return i + 1
    def nextN(n):
        return (n * 252533) % 33554393

    vI = 1
    for y in range(height):
        for i in range(y+1):
            yi,xi = y-i,i
            grid[yi][xi] = value
            value = nextN(value)

    return grid

def getValueFromGrid(x,y):
    total = x+y
    grid = generateCodeField(total,total)
    row = grid[y-1]
    return grid[y-1][x-1]

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    output = getValueFromGrid(inputs[1],inputs[0])

    print "Day 25 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = 0

    print "Day 25 Puzzle 2 Solution - " + str(output)