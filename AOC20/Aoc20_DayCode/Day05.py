import os

def solve():
    fileLoc = "inputs/day05.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        f = file.readline().strip()
        if not f == 'AOC20_INPUT_DAY05':
            print "Invalid input file header: Day05"
            return False
     
        return file.readlines()
    else:
        print "Day 05 input file does not exist"

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    passes = processPasses(inputs)

    output = getMaxID(passes)

    print "Day 05 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    passes = processPasses(inputs)

    output = findSeat(passes)

    print "Day 05 Puzzle 2 Solution - " + str(output)

def processPasses(passes):
    pOut = []
    for l in passes:
        row = []
        seat = []
        for c in l:
            if c == 'F':
                row.append('L')
            elif c == 'B':
                row.append('U')
            elif c == 'L':
                seat.append('L')
            elif c == 'R':
                seat.append('U')
            
        pOut.append( (row,seat) )
    
    return pOut
    
def getSeatID(pos):
    return pos[0] * 8 + pos[1]

def getSeatPos(bPass):
    return (getPosition(bPass[0], 128),getPosition(bPass[1], 8))

def getMaxID(passes):
    output = 0

    for p in passes:
        output = max(getSeatID(getSeatPos(p)),output)

    return output

def getMinID(passes):
    output = 128 * 8 + 8

    for p in passes:
        output = min(getSeatID(getSeatPos(p)),output)

    return output

def getPosition(finder, setSize):
    s = range(setSize)

    for v in finder:
        if v == 'L':
            s = s[:len(s)/2]
        elif v == 'U':
            s = s[len(s)/2:]

        if len(s) == 1:
            return s[0]

    return 0

def findSeat(passes):
    seatIDs = set()

    minID = getMinID(passes)
    maxID = getMaxID(passes)

    # Create a set of valid seat IDs to check against
    for i in range(128):
        for j in range(8):
            newID = getSeatID( (i,j) )
            if newID <= maxID and newID >= minID:
                seatIDs.add(newID)

    # Remove every seat ID we have a pass for
    for p in passes:
        seatIDs.remove(getSeatID(getSeatPos(p)))

    # There should only be one element left in the set, the seat we need
    return seatIDs.pop()