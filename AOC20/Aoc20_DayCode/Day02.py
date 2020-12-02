import os

def solve():
    fileLoc = "inputs/day02.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        f = file.readline().strip()
        if not f == 'AOC20_INPUT_DAY02':
            print "Invalid input file header: Day02"
            return False
     
        return file.readlines()
    else:
        print "Day 02 input file does not exist"

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    pwds = workInputs(inputs)

    for p in pwds:
        if isValidPart1(p):
            output += 1

    print "Day 02 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    pwds = workInputs(inputs)

    for p in pwds:
        if isValidPart2(p):
            output += 1

    print "Day 02 Puzzle 2 Solution - " + str(output)
    
def workInputs(inputs):
    outputs = []

    for i in inputs:
        s = i.split(':')
        pwd = s[1].strip() # The password
        c = s[0].split()[1] # The character to check
        rng = s[0].split()[0] # The valid range
        low = rng.split('-')[0] # The low end of the range
        hi = rng.split('-')[1] # The high end of the range

        outputs.append((int(low),int(hi),c,pwd))

    return outputs

def isValidPart1(pwd):
    c = pwd[3].count(pwd[2])

    if c >= pwd[0] and c <= pwd[1]:
        return True
    else:
        return False

def isValidPart2(pwd):
    fP = pwd[3][pwd[0] - 1] # First char
    sP = pwd[3][pwd[1] - 1] # Second char

    if (fP == pwd[2]) ^ (sP == pwd[2]):
        return True
    else:
        return False