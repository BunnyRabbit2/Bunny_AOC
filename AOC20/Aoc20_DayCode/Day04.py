import os, re

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

    passports = processPassports(inputs)

    for p in passports:
        if isPassportValid(p, True):
            output += 1

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

def isPassportValid(pspt, strict = False):
    if 'byr' in pspt and 'iyr' in pspt and 'eyr' in pspt and 'hgt' in pspt and 'hcl' in pspt and 'ecl' in pspt and 'pid' in pspt:
        if strict:

            byr = int(pspt['byr'])
            if byr < 1920 or byr > 2002:
                return False
            
            iyr = int(pspt['iyr'])
            if iyr < 2010 or iyr > 2020:
                return False

            eyr = int(pspt['eyr'])
            if eyr < 2020 or eyr > 2030:
                return False

            hgt = int(pspt['hgt'][:-2]) # Height as a number
            hgtT = pspt['hgt'][-2:]
            if hgtT == 'cm':
                if hgt < 150 or hgt > 193:
                    return False
            elif hgtT == 'in':
                if hgt < 59 or hgt > 76:
                    return False
            else:
                return False

            hcl = pspt['hcl']
            res = re.findall('#[0-9,a-f]{6}',hcl)
            if len(res) != 1:
                return False

            eclSet = {'amb','blu','brn','gry','grn','hzl','oth'}
            if pspt['ecl'] not in eclSet:
                return False

            pid = pspt['pid']
            if len(pid) != 9:
                return False
            if re.match('[0-9]{9}',pid) is None:
                return False

            return True

        else:
            return True
    else:
        return False