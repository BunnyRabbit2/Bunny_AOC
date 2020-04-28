import os, md5

def solve():
    fileLoc = "inputs/day4.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 4 input file does not exist")

def findAdventCoin(secret, checkString):
    foundCoin = False
    currrentNumber = 0

    while not foundCoin:
        testHash = md5.new(secret + str(currrentNumber)).hexdigest()
        if testHash[0:len(checkString)] == checkString:
            foundCoin = True
        else:
            currrentNumber += 1

    return currrentNumber

def solvePuzzle1(fileLocation):
    input = loadInputs(fileLocation)

    output = findAdventCoin(input, "00000")

    print "Day 4 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    input = loadInputs(fileLocation)

    output = findAdventCoin(input, "000000")

    print "Day 4 Puzzle 2 Solution - " + str(output)