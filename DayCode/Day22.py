import os
from sys import maxsize

p1MinMana = maxsize
finalSpellsUsed = []
magicShort = {
    "Magic_Missile":"MM",
    "Drain":"DD",
    "Recharge":"RE",
    "Shield":"SH",
    "Poison":"PP"
}

def solve():
    fileLoc = "inputs/day22.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split('\n')
    else:
        print("Day 22 input file does not exist")

def createGameData(inputs):
    boss = {}
    magic = {}

    for i in range(len(inputs)):
        if 'BOSS START' in inputs[i]:
            boss["hp"] = int(inputs[i+1].split(': ')[1])
            boss["dam"] = int(inputs[i+2].split(': ')[1])

        if 'MAGIC START' in inputs[i]:
            mC = 1
            m = inputs[i+mC]
            while not m == 'END':
                mS = m.split()
                magic.setdefault(mS[0],{})
                magic[mS[0]]['cost'] = int(mS[1])
                
                firstE = mS[2].split('->')
                magic[mS[0]][firstE[0]] = int(firstE[1])
                if len(mS) > 3:
                    secondE = mS[3].split('->')
                    magic[mS[0]][secondE[0]] = int(secondE[1])
                mC += 1
                m = inputs[i+mC]

    return (boss,magic)

def fight(bossHP,bossD,playerHP,playerM,playerA,magic,manaUsed=0,spellsUsed="",shield=0,poison=0,recharge=0):
    for mk in magic.keys():
        m = magic[mk]

        if mk == 'Drain':
            v = 0

        canCast = False

        if m['cost'] < playerM:
            canCast = True

        if shield > 0:
            playerA = magic['Shield']['ARM']
            shield -= 1
        else:
            playerA = 0

        if poison > 0:
            bossHP -= magic['Poison']['DAM']
            poison -= 1
        
        if recharge > 0:
            playerM += magic['Recharge']['MANA']

        if canCast:
            global magicShort
            spellsUsed += magicShort[mk] + ' -> '

            playerM -= m['cost']
            manaUsed += m['cost']

            if 'EFFECT' in m:
                if 'DAM' in m:
                    poison = m['EFFECT']
                elif 'ARM' in m:
                    shield = m['EFFECT']
                elif 'MANA' in m:
                    recharge = m['EFFECT']
            else:
                if 'DAM' in m:
                    bossHP -= m['DAM']
                if 'HEAL' in m:
                    playerHP += m['HEAL']

        playerHP -= bossD - playerA

        if playerHP <= 0:
            global finalSpellsUsed
            spellsUsed = 'FINAL -  PlayerHP: ' + str(playerHP) + ' BossHP: ' + str(bossHP) + ' Spells: ' + spellsUsed
            print(spellsUsed)
            finalSpellsUsed.append(spellsUsed)
            return -1
        if bossHP <= 0:
            return manaUsed
            global p1MinMana
            if manaUsed < p1MinMana:
                p1MinMana = manaUsed

        fight(bossHP,bossD,playerHP,playerM,playerA,magic,manaUsed,spellsUsed,shield,poison,recharge)

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)

    DATA = createGameData(inputs)
    boss = DATA[0]
    magic = DATA[1]
    player = {'hp': 50,'mana': 500,'arm':0}

    fight(boss['hp'],boss['dam'],player['hp'],player['mana'],player['arm'],magic)
    
    output = p1MinMana

    print "Day 22 Puzzle 1 Solution - " + str(output)
    global finalSpellsUsed
    
    file = open("output/d22/output.txt", "w+")
    for r in finalSpellsUsed:
        file.write(r + '\n')
    file.close()

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)

    DATA = createGameData(inputs)
    boss = DATA[0]

    output = 0

    print "Day 22 Puzzle 2 Solution - " + str(output)