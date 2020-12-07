import os

def solve():
    fileLoc = "inputs/day04.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        f = file.readline().strip()
        if not f == 'AOC20_INPUT_DAY04':
            print "Invalid input file header: Day04"
            return False
     
        return file.read()
    else:
        print "Day 04 input file does not exist"

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    passports = processPassports(inputs)

    for p in passports:
        if isPassportValid(p):
            output += 1

    print "Day 04 Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    print "Day 04 Puzzle 2 Solution - " + str(output)
    
def processPassports(pIn):
    passports = []

    pspts = pIn.split('\n\n')

    for p in pspts:
        newP = {}

        pS = p.replace('\n',' ') # Standardised string
        pL = pS.split() # String as a list

        for i in pL:
            items = i.split(':')
            newP[items[0]] = items[1]

        passports.append(newP)

    return passports

def isPassportValid(pspt):
    if 'byr' in pspt and 'iyr' in pspt and 'eyr' in pspt and 'hgt' in pspt and 'hcl' in pspt and 'ecl' in pspt and 'pid' in pspt:
        return True
    else:
        return False