import os
from PIL import Image
import numpy as np
from re import findall

def solve():
    fileLoc = "inputs/day6.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 6 input file does not exist")

def createCommands(commandStrings):
    # command = ["on/off/toggle", (0,0), (1,1)] EXAMPLE COMMAND
    commands = []

    for l in commandStrings:
        cSplit = l.split()
        newCommand = []
        firstCPos = secondCPos = 0

        if cSplit[0] == "toggle":
            newCommand.append("toggle")
            firstCPos = 1
            secondCPos = 3
        elif cSplit[0] == "turn":
            firstCPos = 2
            secondCPos = 4
            if cSplit[1] == "on":
                newCommand.append("on")
            elif cSplit[1] == "off":
                newCommand.append("off")
        
        firstCS = cSplit[firstCPos].split(",")
        secondCS = cSplit[secondCPos].split(",")

        newCommand.append((int(firstCS[0]), int(firstCS[1])))
        newCommand.append((int(secondCS[0]), int(secondCS[1])))

        commands.append(newCommand)
    
    return commands

def countLightsOn(field):
    size = len(field)
    lightsOn = 0

    for x in range(size):
        for y in range(size):
            if field[x][y] == 1:
                lightsOn += 1

    return lightsOn

def countBrightness(field):
    size = len(field)
    totalB = 0

    for x in range(size):
        for y in range(size):
            totalB += field[x][y]

    return totalB

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    commands = findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", inputs)
    lights = [[0 for i in range(1000)] for j in range(1000)]

    for command, x1, y1, x2, y2 in commands:
        coords = [(x,y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)]
        for x,y in coords:
            if command == "turn on":
                lights[x][y] = 1
            elif command == "turn off":
                lights[x][y] = 0
            elif command == "toggle":
                if lights[x][y] == 1:
                    lights[x][y] = 0
                else:
                    lights[x][y] = 1

    output = countLightsOn(lights)

    Image.fromarray(np.array(lights)).save("lights.png")

    print "Day 6 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    commands = findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", inputs)
    lights = [[0 for i in range(1000)] for j in range(1000)]

    for command, x1, y1, x2, y2 in commands:
        coords = [(x,y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)]
        for x,y in coords:
            if command == "turn on":
                lights[x][y] += 1
            elif command == "turn off":
                lights[x][y] -= 1
                if lights[x][y] < 0:
                    lights[x][y] = 0
            elif command == "toggle":
                lights[x][y] += 2

    output = countBrightness(lights)

    print "Day 6 Puzzle 2 Solution - " + str(output)