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

    output = 0

    passes = processPasses(inputs)

    for p in passes:
        output = max(getSeatID(p),output)

    print "Day 05 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

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
    
def getSeatID(bPass):
    row = getPosition(bPass[0], 128)
    seat = getPosition(bPass[1], 8)

    return row * 8 + seat

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