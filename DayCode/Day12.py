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

def getCountNoRed(json):
    if type(json) in [str,unicode]:
        return 0
    if type(json) in [int,float]:
        return json
    if type(json) is list:
        return sum(map(getCountNoRed,json))
    if type(json) is dict:
        if "red" in json.values():
            return 0
        return sum(map(getCountNoRed,json.iteritems()))
    if type(json) is tuple:
        return sum(map(getCountNoRed,json))

def solvePuzzle1(fileLocation):
    jsonFile = loadInputs(fileLocation)

    output = getCount(jsonFile)

    print "Day 12 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    jsonFile = loadInputs(fileLocation)

    output = getCountNoRed(jsonFile)

    print "Day 12 Puzzle 2 Solution - " + str(output)