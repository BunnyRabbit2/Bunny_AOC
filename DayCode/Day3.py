import os

def solve():
    fileLoc = "inputs/day3.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 3 input file does not exist")

def processRoute(route):
    currentX = 0
    currentY = 0
    houses = []
    houses.append((currentX,currentY))

    for h in route:
        if h == '<':
            currentX -= 1
        elif h == '^':
            currentY += 1
        elif h == '>':
            currentX += 1
        elif h == 'v':
            currentY -= 1
        
        if (currentX,currentY) not in houses:
            houses.append((currentX,currentY))

    return (len(houses),0)

def solvePuzzle1(fileLocation):
    input = loadInputs(fileLocation)

    output = processRoute(input)

    print "Day 3 Puzzle 1 Solution - " + str(output[0])

def solvePuzzle2(fileLocation):
    input = loadInputs(fileLocation)

    output = (0,0)

    print "Day 3 Puzzle 2 Solution - " + str(output[1])