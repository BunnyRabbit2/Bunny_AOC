import os
import operator

def solve():
    fileLoc = "inputs/day14.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.readlines()
    else:
        print("Day 14 input file does not exist")

def createReindeerStats(inputs):
    reindeer = {}
    for l in inputs:
        rS = l.split()
        reindeer.setdefault(rS[0],{})
        n = rS[0]
        s = int(rS[3])
        t = int(rS[6])
        r = int(rS[13])
        reindeer[n]["speed"] = s
        reindeer[n]["time"] = t
        reindeer[n]["rest"] = r
        reindeer[n]["stepTime"] = r + t
        reindeer[n]["stepDist"] = s * t
    return reindeer

def findDistanceInTime(time, r):
    steps = time / r["stepTime"]
    if time % r["stepTime"] > r["time"]:
        steps += 1

    return steps * r["stepDist"]

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    rs = createReindeerStats(inputs)

    raceTime = 2503

    distances = {}

    for r in rs:
        d = findDistanceInTime(raceTime, rs[r])
        distances[r] = d

    output = max(distances.iteritems(), key = operator.itemgetter(1))

    print "Day 14 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = 0

    print "Day 14 Puzzle 2 Solution - " + str(output)