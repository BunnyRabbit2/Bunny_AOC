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

def move(command):
    moveX = moveY = 0
    if command == '<':
        moveX -= 1
    elif command == '^':
        moveY += 1
    elif command == '>':
        moveX += 1
    elif command == 'v':
        moveY -= 1

    return (moveX,moveY)

def processRoute(route):
    currentX = 0
    currentY = 0
    houses = []
    houses.append((currentX,currentY))

    for h in route:
        m = move(h)
        currentX += m[0]
        currentY += m[1]
        
        if (currentX,currentY) not in houses:
            houses.append((currentX,currentY))

    return len(houses)

def ProcessRouteAlt(route):
    santaX = 0
    santaY = 0
    roboSantaX = 0
    roboSantaY = 0
    houses = []
    houses.append((santaX,santaY))
    moveRoboSanta = False

    for h in route:
        m = move(h)
        
        if moveRoboSanta:
            roboSantaX += m[0]
            roboSantaY += m[1]

            if (roboSantaX,roboSantaY) not in houses:
                houses.append((roboSantaX,roboSantaY))

            moveRoboSanta = False
        else:
            santaX += m[0]
            santaY += m[1]

            if (santaX,santaY) not in houses:
                houses.append((santaX,santaY))

            moveRoboSanta = True

    return len(houses)

def solvePuzzle1(fileLocation):
    input = loadInputs(fileLocation)

    output = processRoute(input)

    print "Day 3 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    input = loadInputs(fileLocation)

    output = ProcessRouteAlt(input)

    print "Day 3 Puzzle 2 Solution - " + str(output)