import os
import json

def solve():
    fileLoc = "inputs/day12.json"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return json.loads(file.read())
    else:
        print("Day 12 input file does not exist")

def countHook(obj):
    return obj

def getCount(json):
    if type(json) in [str,unicode]:
        return 0
    if type(json) in [int,float]:
        return json
    if type(json) is list:
        return sum(map(getCount,json))
    if type(json) is dict:
        return sum(map(getCount,json.iteritems()))
    if type(json) is tuple:
        return sum(map(getCount,json))

def solvePuzzle1(fileLocation):
    jsonFile = loadInputs(fileLocation)

    output = getCount(jsonFile)

    print "Day 12 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = (0,0)

    print "Day 12 Puzzle 2 Solution - " + str(output[1])