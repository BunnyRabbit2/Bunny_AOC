import os
import re

def solve():
    fileLoc = "inputs/day11.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read()
    else:
        print("Day 11 input file does not exist")

def incrementString(s):
    r = list(s)[::-1]
    i = 0
    for c in r:
        if c == 'z':
            r[i] = 'a'
        else:
            r[i] = chr(ord(c)+1)
            break
        i += 1
    
    return ''.join(r[::-1])

def checkPassword(s):
    if 'i' in s or 'o' in s or 'l' in s:
        return False

    hasStraight = False

    for i in range(len(s)-2):
        if ord(s[i]) == ord(s[i+1]) - 1 and ord(s[i]) == ord(s[i+2]) - 2:
            hasStraight = True

    if not hasStraight:
        return False

    rC = re.findall(r'(.)\1', s)
    if len(rC) < 2:
        return False

    return True

def getNextPassword(s):
    valid = False

    while not valid:
        s = incrementString(s)
        valid = checkPassword(s)

    return s

def solvePuzzle1(fileLocation):
    input = loadInputs(fileLocation)

    output = getNextPassword(input)

    print "Day 11 Puzzle 1 Solution - " + output

def solvePuzzle2(fileLocation):
    input = loadInputs(fileLocation)

    output = getNextPassword(input)
    output = getNextPassword(output)

    print "Day 11 Puzzle 2 Solution - " + output