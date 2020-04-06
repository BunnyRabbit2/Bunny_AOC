import os

def solve():
    fileLoc = "inputs/day15.txt"
    testSolution()
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        return file.read().split("\n")
    else:
        print("Day 15 input file does not exist")

def createIngredients(inputs):
    ingredients = {}

    for l in inputs:
        ing = l.split(": ")[0]
        values = l.split(": ")[1].split(", ")
        ingredients.setdefault(ing,{})

        for v in values:
            ingredients[ing][v.split()[0]] = int(v.split()[1])

    return ingredients

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    ings = createIngredients(inputs)

    score = 0
    maxScore = 0

    for i in range(0,100):
        for j in range(0,100-i):
            for k in range(0,100-i-j):
                h = 100-i-j-k

                cl1,cl2,cl3,cl4 = ings["Sprinkles"]["calories"], ings["Butterscotch"]["calories"], ings["Chocolate"]["calories"], ings["Candy"]["calories"]
                cp1,cp2,cp3,cp4 = ings["Sprinkles"]["capacity"], ings["Butterscotch"]["capacity"], ings["Chocolate"]["capacity"], ings["Candy"]["capacity"]
                d1,d2,d3,d4 = ings["Sprinkles"]["durability"], ings["Butterscotch"]["durability"], ings["Chocolate"]["durability"], ings["Candy"]["durability"]
                f1,f2,f3,f4 = ings["Sprinkles"]["flavor"], ings["Butterscotch"]["flavor"], ings["Chocolate"]["flavor"], ings["Candy"]["flavor"]
                t1,t2,t3,t4 = ings["Sprinkles"]["texture"], ings["Butterscotch"]["texture"], ings["Chocolate"]["texture"], ings["Candy"]["texture"]

                cal = cl1*i + cl2*j + cl3*k + cl4*h
                cap = cp1*i + cp2*j + cp3*k + cp4*h
                dur = d1*i + d1*j + d3*k + d4*h
                fla = f1*i + f1*j + f3*k + f4*h
                tex = t1*i + t1*j + t3*k + t4*h

                score = cap * dur * fla * tex

                maxScore = max(score,maxScore)
                

    print "Day 15 Puzzle 1 Solution - " + '{:,}'.format(maxScore)

def solvePuzzle2(fileLocation):
    # inputs = loadInputs(fileLocation)

    output = 0

    print "Day 15 Puzzle 2 Solution - " + str(output)

def testSolution():
    t = [[2,0,-2,0,3],[0,5,-3,0,3],[0,0,5,-1,8],[0,-1,0,5,8]]

    score = 0 
    maxS = 0
    for i in range(0,100):
        for j in range(0,100-i):
            for k in range(0,100-i-j):
                h = 100-i-j-k
                a = t[0][0]*i+t[1][0]*j+t[2][0]*k+t[3][0]*h
                b = t[0][1]*i+t[1][1]*j+t[2][1]*k+t[3][1]*h
                c = t[0][2]*i+t[1][2]*j+t[2][2]*k+t[3][2]*h
                d = t[0][3]*i+t[1][3]*j+t[2][3]*k+t[3][3]*h
                e = t[0][4]*i+t[1][4]*j+t[2][4]*k+t[3][4]*h

                #extra condition for part b
                if(not(e == 500)):
                    continue
                if (a <= 0 or b <= 0 or c <= 0 or d <= 0):
                    score = 0
                    continue
                score = a*b*c*d
                if (score > maxS):
                    maxS = score
    print maxS