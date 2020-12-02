import os, sys, re

year = str(sys.argv[1])

def createInitPy():
    f = open('__init__.py','w+')
    f.close()

def createGitignore():
    f = open('.gitignore','w+')
    f.write('''### Python ###
__pycache__/
*.py[cod]
*$py.class

*.so

.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

*.manifest
*.spec

pip-log.txt
pip-delete-this-directory.txt

htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

*.mo
*.pot

.scrapy

docs/_build/

target/

.python-version

celerybeat-schedule

*.sage.py

.spyderproject
.spyproject

.ropeproject

.mr.developer.cfg
.project
.pydevproject

/site

.mypy_cache/
.dmypy.json
dmypy.json

.pyre/

# User Additions
bash.exe.stackdump
lights.png
/output/*
    ''')
    f.close()

def createMain():
    global year
    f = open('main.py','w+')
    mainS = '''from Aoc{YEAR}_DayCode import Day01
import Aoc{YEAR}_SolveAll
import os

def main():
    print "Starting Advent of Code 20{YEAR} program - Python 2.7 Version"
    os.chdir('AOC{YEAR}')
    Day01.solve()
    # SolveAll.SolveAll()

if __name__ == "__main__":
    main()
    '''
    mainS = mainS.replace('{YEAR}',year)
    f.write(mainS)
    f.close()

def createReadme():
    global year
    f = open('README.md','w+')
    readmeS = '''# BunnyAoC20{YEAR} Python version

This program will solve all of the problems presented by the Advent of Code 20{YEAR} which can be found at <https://adventofcode.com/20{YEAR}>

Each day code script will output the answer to each puzzle into the console with a label to identify what puzzle the solution is for.

The AocYEAR_SolveAll.py script will use the day code scripts and reroute the outputs into a text file
    '''
    readmeS = readmeS.replace('{YEAR}',year)
    f.write(readmeS)
    f.close()

def createSolveAll():
    global year
    f = open('Aoc'+year+'_SolveAll.py','w+')
    solveAllS = '''from Aoc{YEAR}_DayCode import Day01,Day02,Day03,Day04,Day05,Day06,Day07,Day08,Day09,Day10,Day11,Day12,Day13,Day14,Day15,Day16,Day17,Day18,Day19,Day20,Day21,Day22,Day23,Day24,Day25
import StringIO, sys, io

def SolveAll():
    out = StringIO.StringIO()
    sys.stdout = out

    Day1.solve()
    Day2.solve()
    Day3.solve()
    Day4.solve()
    Day5.solve()
    Day6.solve()
    Day7.solve()
    Day8.solve()
    Day9.solve()
    Day10.solve()
    Day11.solve()
    Day12.solve()
    Day13.solve()
    Day14.solve()
    Day15.solve()
    Day16.solve()
    Day17.solve()
    Day18.solve()
    Day19.solve()
    Day20.solve()
    Day21.solve()
    Day22.solve()
    Day23.solve()
    Day24.solve()
    Day25.solve()

    file = open("aoc{YEAR}_puzzle_solutions.txt", "w+")
    for l in out.buflist:
        file.write(l)
    file.close()
    '''
    solveAllS = solveAllS.replace('{YEAR}',year)
    f.write(solveAllS)
    f.close()

def createInputFiles():
    global year
    inputD = 'inputs'
    os.mkdir(inputD)
    os.chdir(inputD)

    for i in range(1,26):
        fileN = "%02d" % (i,)
        f = open('day'+fileN+'.txt','w+')
        f.write('AOC'+year+'_INPUT_DAY' + fileN)
        f.close()

    os.chdir('..')

def createDayCode():
    global year
    daycodeD = 'Aoc'+year+'_DayCode'
    os.mkdir(daycodeD)
    os.chdir(daycodeD)

    createInitPy()

    for i in range(1,26):
        fileN = "%02d" % (i,)
        f = open('Day'+fileN+'.py','w+')
        daycodeS = '''import os

def solve():
    fileLoc = "inputs/day{FILEN}.txt"
    solvePuzzle1(fileLoc)
    solvePuzzle2(fileLoc)

def loadInputs(fileLocation):
    if os.path.exists(fileLocation):
        file = open(fileLocation)
        f = file.readline().strip()
        if not f == 'AOC{YEAR}_INPUT_DAY{FILEN}':
            print "Invalid input file header: Day{FILEN}"
            return False
     
        return file.read()
    else:
        print "Day {FILEN} input file does not exist"

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    print "Day {FILEN} Puzzle 1 Solution - " + str(output)

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    if inputs == '':
        return

    output = 0

    print "Day {FILEN} Puzzle 2 Solution - " + str(output)
    '''
        daycodeS = daycodeS.replace('{YEAR}',year).replace('{FILEN}',fileN)
        f.write(daycodeS)
        f.close()

    os.chdir('..')

year = sys.argv[1]

topDirP = 'AOC'+year

os.mkdir(topDirP)
os.chdir(topDirP)

createInitPy()
createGitignore()
createMain()
createSolveAll()
createInputFiles()
createDayCode()