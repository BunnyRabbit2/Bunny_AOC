import os
from PIL import Image
import numpy as np

def solve():
    fileLoc = "inputs/day6.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.readlines()
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

def createLightField():
    size = 1000
    field = []

    for x in range(size):
        newCol = []
        for y in range(size):
            newCol.append(False)
        field.append(newCol)

    return field

def runCommand(command, field):
    for x in range(command[1][0],command[2][0]):
        for y in range(command[1][1],command[2][1]):
            if command[0] == "on":
                field[x][y] = True
            elif command[0] == "off":
                field[x][y] = False
            elif command[0] == "toggle":
                field[x][y] = not field[x][y]

    # writeLightFile(field)
    Image.fromarray(np.array(field)).save("lights.png")

    return field

def countLightsOn(field):
    size = len(field)
    lightsOn = 0

    for x in range(size):
        for y in range(size):
            if field[x][y]:
                lightsOn += 1

    return lightsOn

def writeLightFile(field):
    on = "0"
    off = " "
    size = len(field)
    lines = []

    for y in range(size):
        line = ""
        for x in range(size):
            if field[x][y]:
                line += on
            else:
                line += off
        lines.append(line)

    with open('testlights.txt', 'w') as f:
        for l in lines:
            print >> f, l
                

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    commands = createCommands(inputs)
    lights = createLightField()

    for c in commands:
        lights = runCommand(c,lights)

    output = countLightsOn(lights)

    print "Day 6 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = (0,0)

    print "Day 6 Puzzle 2 Solution - " + str(output[1])