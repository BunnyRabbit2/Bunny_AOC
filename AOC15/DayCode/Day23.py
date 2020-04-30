import os

def solve():
    fileLoc = "inputs/day23.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split('\n')
    else:
        print("Day 23 input file does not exist")

def createInstructionList(inputs):
    instructions = []
    for ins in inputs:
        insS = ins.split()
        ins1 = ''
        ins2 = 0

        if insS[1] == 'a' or insS[1] == 'b':
            ins1 = insS[1]
        else:
            ins1 = int(insS[1][1:])
            if insS[1][0] == '-':
                ins1 *= -1

        if len(insS) > 2:
            ins2 = int(insS[2][1:])
            if insS[2][0] == '-':
                ins2 *= -1
        newInstruction = (insS[0],ins1,ins2)
        instructions.append(newInstruction)
    return instructions

def runInstructions(instructions,startingRegs=(0,0)):
    regA, regB = startingRegs[0],startingRegs[1]
    nextI = 0

    while nextI < len(instructions):
        ins = instructions[nextI]

        if ins[0] == 'hlf':
            if ins[1] == 'a':
                regA /= 2
            elif ins[1] == 'b':
                regB /= 2
        elif ins[0] == 'tpl':
            if ins[1] == 'a':
                regA *= 3
            elif ins[1] == 'b':
                regB *= 3
        elif ins[0] == 'inc':
            if ins[1] == 'a':
                regA += 1
            elif ins[1] == 'b':
                regB += 1
        elif ins[0] == 'jmp':
            nextI += ins[1]
            continue
        elif ins[0] == 'jie':
            if ins[1] == 'a':
                if regA % 2 == 0:
                    nextI += ins[2]
                    continue
            elif ins[1] == 'b':
                if regB % 2 == 0:
                    nextI += ins[2]
                    continue
        elif ins[0] == 'jio':
            if ins[1] == 'a':
                if regA == 1:
                    nextI += ins[2]
                    continue
            elif ins[1] == 'b':
                if regB == 1:
                    nextI += ins[2]
                    continue
        
        nextI += 1

    return (regA,regB)

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    instructions = createInstructionList(inputs)

    output = runInstructions(instructions)

    print "Day 23 Puzzle 1 Solution - " + str(output[1])

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    instructions = createInstructionList(inputs)

    output = runInstructions(instructions,(1,0))

    print "Day 23 Puzzle 2 Solution - " + str(output[1])