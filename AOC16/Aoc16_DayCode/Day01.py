import os

def solve():
    fileLoc = "inputs/day01.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        f = file.readline().strip()
        if not f == 'AOC16_INPUT_DAY01':
            print "Invalid input file header: Day01"
            return ''
     
        return file.read().split(', ')
    else:
        print "Day 01 input file does not exist"

def findDistanceToBase(steps):
    posStack = []
    foundAns2 = False
    ans2 = (0,0)

    x,y = 0,0
    direction = 0 # 0 N, 1 E, 2 S, 3 W
    def turnRight(d):
        d += 1
        if d > 3: d = 0
        return d
    def turnLeft(d):
        d -= 1
        if d < 0: d = 3
        return d

    for c in steps:
        if c[0] == 'L':
            direction = turnLeft(direction)
        elif c[0] == 'R':
            direction = turnRight(direction)

        for _ in range(int(c[1:])):
            if direction == 0: y += 1
            elif direction == 1: x += 1
            elif direction == 2: y -= 1
            elif direction == 3: x -= 1

            if (x,y) in posStack and not foundAns2:
                ans2 = abs(x)+abs(y)
                foundAns2 = True
            else:
                posStack.append((x,y))

    return (abs(x)+abs(y),ans2)

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = findDistanceToBase(inputs)[0]

    print "Day 01 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = findDistanceToBase(inputs)[1]

    print "Day 01 Puzzle 2 Solution - " + str(output)
    