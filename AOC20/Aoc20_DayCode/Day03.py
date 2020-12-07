import os

def solve():
    fileLoc = "inputs/day03.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        f = file.readline().strip()
        if not f == 'AOC20_INPUT_DAY03':
            print "Invalid input file header: Day03"
            return False
     
        return file.readlines()
    else:
        print "Day 03 input file does not exist"

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    grid = createTreeGrid(inputs)

    output = getTreesHit(grid,3,1)

    print "Day 03 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 1

    grid = createTreeGrid(inputs)

    res = []
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

    for s in slopes:
        res.append(getTreesHit(grid,s[0],s[1]))

    for r in res:
        output *= r

    print "Day 03 Puzzle 2 Solution - " + str(output)
    
def createTreeGrid(input):
    grid = []

    for l in input:
        line = []
        for c in l:
            if c == '#':
                line.append(True)
            elif c == '.':
                line.append(False)
        grid.append(line)

    return grid

def getTreesHit(grid,speedx,speedy):
    output = 0
    x = 0
    y = 0

    length = len(grid)
    width = len(grid[0])

    while True:
        x += speedx
        y += speedy

        if x >= width:
            x -= width
        
        if y >= length:
            break

        if grid[y][x]:
            output += 1

    return output