import os

def solve():
    fileLoc = "inputs/day7.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.readlines()
    else:
        print("Day 7 input file does not exist")

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def createGateList(inputs):
    GATE_ID = 0

    gateList = {}

    for c in inputs:
        inSignal = -1
        inWire = "NIL"
        inWire2 = "NIL"
        gateT = "T0"
        gateV = -1

        output = c.split("->")[1].strip()
        command = c.split("->")[0].split()
        if len(command) == 1:
            if is_int(command[0]):
                inSignal = int(command[0])
            else:
                inWire = command[0]
                gateT = "DIODE"
        elif command[1] == "AND":
            inWire = command[0]
            inWire2 = command[2]
            gateT = command[1]
        elif command[1] == "OR":
            inWire = command[0]
            inWire2 = command[2]
            gateT = command[1]
        elif command[0] == "NOT":
            inWire = command[1]
            gateT = command[1]
        elif command[1] == "LSHIFT":
            inWire = command[0]
            gateT = command[1]
            gateV = int(command[2])
        elif command[1] == "RSHIFT":
            inWire = command[0]
            gateT = command[1]
            gateV = int(command[2])

        gateList[GATE_ID] = {
            "type":gateT,
            "value":gateV,
            "inWire1":inWire,
            "inWire2":inWire2,
            "inSignal":inSignal,
            "outWire":output,
            "outSignal":0
        }
        # gateList[GATE_ID] = (gateT, gateV, inWire, inWire2, inSignal, output, 0)
        GATE_ID += 1

    return gateList

def calculateIn(gate):
    if gate[0] == "DIODE":
        return
    elif gate[1] == "AND":
        return
    elif gate[1] == "OR":
        return
    elif gate[1] == "NOT":
        return
    elif gate[1] == "LSHIFT":
        return
    elif gate[1] == "RSHIFT":
        return

def calculateOut(gate):
    if gate[0] == "DIODE":
        return
    elif gate[1] == "AND":
        return
    elif gate[1] == "OR":
        return
    elif gate[1] == "NOT":
        return
    elif gate[1] == "LSHIFT":
        return
    elif gate[1] == "RSHIFT":
        return

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    gateList = createGateList(inputs)

    output = (0,0)

    print "Day 7 Puzzle 1 Solution - " + str(output[0])

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = (0,0)

    print "Day 7 Puzzle 2 Solution - " + str(output[1])