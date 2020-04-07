import os

def solve():
    fileLoc = "inputs/day18.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split('\n')
    else:
        print("Day 18 input file does not exist")

def createGrid(inputs, width):
    grid = []
    for x in range(width):
        column = []
        for y in range(width):
            column.append("")
        grid.append(column)
    
    for y in range(len(inputs)):
        line = list(inputs[y])
        for x in range(len(line)):
            grid[x][y] = line[x]

    return grid

def stepLightGrid(grid):
    size = len(grid)
    newGrid = []
    for x in range(size):
        column = []
        for y in range(size):
            column.append("")
        newGrid.append(column)

    def isValid(x,y):
        return x >= 0 and x < size and y >= 0 and y < size

    for x in range(size):
        for y in range(size):
            toCheck = []
            for i in range(-1,2):
                for j in range(-1,2):
                    if not i == 0 or not j == 0:
                        cX = x + i
                        cY = y + j
                        if isValid(cX,cY):
                            toCheck.append((cX,cY))
            lightsOn = 0
            for tC in toCheck:
                if grid[tC[0]][tC[1]] == '#':
                    lightsOn += 1
            if grid[x][y] == '#':
                if lightsOn == 2 or lightsOn == 3:
                    newGrid[x][y] = '#'
                else:
                    newGrid[x][y] = '.'
            else:
                if lightsOn == 3:
                    newGrid[x][y] = '#'
                else:
                    newGrid[x][y] = '.'

    return newGrid

def countLightsOn(grid):
    size = len(grid)

    lightsOn = 0

    for x in range(size):
        for y in range(size):
            if grid[x][y] == '#':
                lightsOn += 1

    return lightsOn

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    grid = createGrid(inputs,100)

    for i in range(100):
        grid = stepLightGrid(grid)

    output = countLightsOn(grid)

    print "Day 18 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = 0

    print "Day 18 Puzzle 2 Solution - " + str(output)