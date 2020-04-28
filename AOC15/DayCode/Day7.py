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
        gateV = None

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
            gateT = command[0]
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
            "outSignal":None,
        }

    return gateList

def calculateIn(gate, gateList):
    gateO = gateList[gate]

    if is_int(gateO["inWire1"]):
        gateO["outSignal"] = int(gateO["inWire1"])
        return

    if gateList[gateO["inWire1"]]["outSignal"] == None:
        calculateIn(gateO["inWire1"], gateList)
    if gateO["inWire2"] != "NIL":
        if gateList[gateO["inWire2"]]["outSignal"] == None:
            calculateIn(gateO["inWire2"], gateList)

    out = -1
    iw2o = -1

    iw1o = gateList[gateO["inWire1"]]["outSignal"]
    if gateO["inWire2"] != "NIL":
        iw2o = gateList[gateO["inWire2"]]["outSignal"]

    if gateO["type"] == "DIODE":
        out = iw1o
    elif gateO["type"] == "AND":
        out = iw1o & iw2o
    elif gateO["type"] == "OR":
        out = iw1o | iw2o
    elif gateO["type"] == "NOT":
        out = ~iw1o
    elif gateO["type"] == "LSHIFT":
        out = iw1o << gateO["value"]
    elif gateO["type"] == "RSHIFT":
        out = iw1o >> gateO["value"]

    gateO["outSignal"] = out

def calculateOut(gate, gateList):
    gateO = gateList[gate]

    if is_int(gateO["inWire1"]):
        gateO["outSignal"] = int(gateO["inWire1"])
        return

    if gateList[gateO["inWire1"]]["outSignal"] == None:
        calculateIn(gateO["inWire1"], gateList)
    if gateO["inWire2"] != "NIL":
        if gateList[gateO["inWire2"]]["outSignal"] == None:
            calculateIn(gateO["inWire2"], gateList)

    out = -1
    iw2o = -1

    iw1o = gateList[gateO["inWire1"]]["outSignal"]
    if gateO["inWire2"] != "NIL":
        iw2o = gateList[gateO["inWire2"]]["outSignal"]

    if gateO["type"] == "DIODE":
        out = iw1o
    elif gateO["type"] == "AND":
        out = iw1o & iw2o
    elif gateO["type"] == "OR":
        out = iw1o | iw2o
    elif gateO["type"] == "NOT":
        out = ~iw1o
    elif gateO["type"] == "LSHIFT":
        out = iw1o << gateO["value"]
    elif gateO["type"] == "RSHIFT":
        out = iw1o >> gateO["value"]

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