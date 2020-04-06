import os

def solve():
    fileLoc = "inputs/day16.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split('\n')
    else:
        print("Day 16 input file does not exist")

def createSues(inputs):
    sues = []

    def isADog(d):
        return d == "samoyeds" or d == "pomeranians" or d == "akitas" or d == "vizalas"

    for s in inputs:
        sA = s.replace(":","").replace(",","")
        sA = sA.split()
        sue = {
            "children": 0,
            "cats": 0,
            "samoyeds": 0,
            "pomeranians": 0,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 0,
            "trees": 0,
            "cars": 0,
            "perfumes": 0
        }
        sue[sA[2]] = int(sA[3])
        sue[sA[4]] = int(sA[5])
        sue[sA[6]] = int(sA[7])

        # sue["dogs"] = 0
        # for i in range(2,8,2):
        #     if isADog(sA[i]):
        #         sue["dogs"] += int(sA[i+1])

        sues.append(sue)

    return sues

def findNumberSue(sues, checkSue):
    sueN = 0
    possibleSues = []

    for i in range(len(sues)):
        s = sues[i]

        goodSue = True

        ks = s.keys()

        matchCount = 0

        for j in range(len(ks)):
            if s[ks[j]] == checkSue[ks[j]]:
                matchCount += 1

        if matchCount > 4:
            possibleSues.append((s,matchCount))
            sueN = i

    return sueN

def findNumberSueAlt(sues, checkSue):
    sueN = 0
    possibleSues = []

    for i in range(len(sues)):
        s = sues[i]

        goodSue = True

        ks = s.keys()

        matchCount = 0

        for j in range(len(ks)):
            k = ks[j]
            if k == "cats" or k == "trees":
                if s[k] > checkSue[k]:
                    matchCount += 1
            elif k == "pomeranians" or k == "goldfish":
                if s[k] < checkSue[k]:
                    matchCount += 1
            elif s[k] == checkSue[k]:
                matchCount += 1

        if matchCount > 6:
            possibleSues.append((s,matchCount))
            sueN = i

    return sueN

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    sues = createSues(inputs)

    checkSue = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }

    output = findNumberSue(sues, checkSue)

    print "Day 16 Puzzle 1 Solution - " + str(output + 1) # correcting for 0 index

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    sues = createSues(inputs)

    checkSue = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }

    output = findNumberSueAlt(sues, checkSue)

    print "Day 16 Puzzle 2 Solution - " + str(output + 1) # correcting for 0 index