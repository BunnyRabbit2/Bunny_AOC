import os

def solve():
    fileLoc = "inputs/day5.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split()
    else:
        print("Day 5 input file does not exist")

def checkStringIsNice(testString):
    hasPair = False
    naughtyPairs = ["ab","cd","pq","xy"]
    vowels = []
    vowelCheck = ["a","e","i","o","u"]

    for i in range(len(testString)):
        pairCheck = testString[i:i+2]
        if pairCheck in naughtyPairs:
            return False

        if len(pairCheck) > 1:
            if pairCheck[0] == pairCheck[1]:
                hasPair = True

        char = testString[i]

        if char in vowelCheck:
            vowels.append(char)

    if hasPair and len(vowels) >= 3:
        return True
    else:
        return False

def checkStringIsNiceAlt(testString):
    hasRepeatPair = False
    hasTripleSet = False

    for i in range(len(testString)):
        testPair = testString[i:i+2]
        if len(testPair) > 1:
            newTestString = testString
            newTestString = newTestString[:i] + "--" + newTestString[i + 2:]

            for j in range(len(testString)):
                newTestPair = newTestString[j:j+2]
                if newTestPair == testPair:
                    hasRepeatPair = True
            
        checkTriple = testString[i:i+3]
        if len(checkTriple) > 2:
            if checkTriple[0] == checkTriple[2] and checkTriple[0] != checkTriple[1]:
                hasTripleSet = True

    if hasTripleSet and hasRepeatPair:
        return True
    else:
        return False

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    niceStrings = 0

    for s in inputs:
        if checkStringIsNice(s):
            niceStrings += 1

    print "Day 5 Puzzle 1 Solution - " + str(niceStrings)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    niceStrings = 0

    for s in inputs:
        if checkStringIsNiceAlt(s):
            niceStrings += 1

    print "Day 5 Puzzle 2 Solution - " + str(niceStrings)