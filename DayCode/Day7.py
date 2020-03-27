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
    gateList = {}

    for c in inputs:
        inWire = "NIL"
        inWire2 = "NIL"
        gateT = "T0"
        gateV = -1

        output = c.split("->")[1].strip()
        command = c.split("->")[0].split()
        if len(command) == 1:
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

        gateList[output] = {
            "type":gateT,
            "value":gateV,
            "inWire1":inWire,
            "inWire2":inWire2,
            "outSignal":-1,
        }

    return gateList

def calculateIn(gate, gateList):
    gateO = gateList[gate]

    if is_int(gateO["inWire1"]):
        gateO["outSignal"] = int(gateO["inWire1"])
        return

    if gateList[gateO["inWire1"]]["outSignal"] == -1:
        calculateIn(gateO["inWire1"], gateList)
    if gateO["inWire2"] != "NIL":
        if gateList[gateO["inWire2"]]["outSignal"] == -1:
            calculateIn(gateO["inWire2"], gateList)

    out = -1

    if gateO["type"] == "DIODE":
        out = gateList[gateO["inWire1"]]["outSignal"]
    elif gateO["type"] == "AND":
        out = gateList[gateO["inWire1"]]["outSignal"] & gateList[gateO["inWire2"]]["outSignal"]
    elif gateO["type"] == "OR":
        out = gateList[gateO["inWire1"]]["outSignal"] | gateList[gateO["inWire2"]]["outSignal"]
    elif gateO["type"] == "NOT":
        out = ~gateList[gateO["inWire1"]]["outSignal"]
    elif gateO["type"] == "LSHIFT":
        out = gateList[gateO["inWire1"]]["outSignal"] << gateO["value"]
    elif gateO["type"] == "RSHIFT":
        out = gateList[gateO["inWire1"]]["outSignal"] >> gateO["value"]

    gateO["outSignal"] = out

def calculateOut(gate, gateList):
    gateO = gateList[gate]

    if gateList[gateO["inWire1"]]["outSignal"] == -1:
        calculateIn(gateO["inWire1"], gateList)
    if gateO["inWire2"] != "NIL":
        if gateList[gateO["inWire2"]]["outSignal"] == -1:
            calculateIn(gateO["inWire2"], gateList)

    out = -1

    if gateO["type"] == "DIODE":
        out = gateList[gateO["inWire1"]]["outSignal"]
    elif gateO["type"] == "AND":
        out = gateList[gateO["inWire1"]]["outSignal"] & gateList[gateO["inWire2"]]["outSignal"]
    elif gateO["type"] == "OR":
        out = gateList[gateO["inWire1"]]["outSignal"] | gateList[gateO["inWire2"]]["outSignal"]
    elif gateO["type"] == "NOT":
        out = ~gateList[gateO["inWire1"]]["outSignal"]
    elif gateO["type"] == "LSHIFT":
        out = gateList[gateO["inWire1"]]["outSignal"] << gateO["value"]
    elif gateO["type"] == "RSHIFT":
        out = gateList[gateO["inWire1"]]["outSignal"] >> gateO["value"]

    gateO["outSignal"] = out

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    gateList = createGateList(inputs)
    wires = {}

    calculateOut("a", gateList)

    output = gateList["a"]

    print "Day 7 Puzzle 1 Solution - " + str(output["outSignal"])

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = (0,0)

    print "Day 7 Puzzle 2 Solution - " + str(output[1])