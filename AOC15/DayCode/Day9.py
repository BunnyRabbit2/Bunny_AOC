import os
from itertools import permutations

def solve():
    fileLoc = "inputs/day9.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.readlines()
    else:
        print("Day 9 input file does not exist")

def findDistances(inputs):
    places = set()
    distances = {}

    for s in inputs:
        (source, _, dest, _, distance) = s.split()
        places.add(source)
        places.add(dest)
        distances.setdefault(source, {})[dest] = int(distance)
        distances.setdefault(dest, {})[source] = int(distance)

    shortest = -1
    longest = 0

    for items in permutations(places):
        dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
        if shortest == -1:
            shortest = dist
        shortest = min(shortest,dist)
        longest = max(longest,dist)

    return (shortest,longest)

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    output = findDistances(inputs)

    print "Day 9 Puzzle 1 Solution - " + str(output[0])

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    output = findDistances(inputs)

    print "Day 9 Puzzle 2 Solution - " + str(output[1])