import os

def solve():
    fileLoc = "inputs/day20.txt"
    #solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 20 input file does not exist")

def solvePuzzle1(fileLocation):
    inputs = int(loadInputs(fileLocation))

    houseN = 1000000

    output = 0

    houses = []
    for i in range(houseN):
        houses.append(0)

    for i in range(1,len(houses)):
        for j in range(i,len(houses),i):
            houses[j] += i * 10

    for i in range(1,len(houses)):
        if houses[i] >= inputs:
            output = i
            break

    print "Day 20 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = int(loadInputs(fileLocation))

    houseN = 1000000

    output = 0

    houses = []
    for i in range(houseN):
        houses.append(0)

    for i in range(1,len(houses)):
        houseCount = 0
        for j in range(i,len(houses),i):
            houses[j] += i * 11
            houseCount += 1
            if houseCount >= 50:
                break

    for i in range(1,len(houses)):
        if houses[i] >= inputs:
            houseV = houses[i]
            output = i
            break

    print "Day 20 Puzzle 2 Solution - " + str(output)