import os
import sys
import re

year = str(sys.argv[1])


def create_init_py():
    f = open('__init__.py', 'w+')
    f.close()


def create_gitignore():
    f = open('.gitignore', 'w+')
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


def create_main():
    global year
    f = open('main.py', 'w+')
    main_str = f'''from aoc_{year}_day_code import day_01
import aoc_{year}_solve_all
import os

def main():
    print("Starting Advent of Code 20{year} program - Python 2.7 Version")
    os.chdir('AOC{year}')
    day_01.solve()
    # solve_all.solve_all()

if __name__ == "__main__":
    main()
    '''
    f.write(main_str)
    f.close()


def create_readme():
    global year
    f = open('README.md', 'w+')
    readme_str = f'''# Bunny Advent of Code 20{year} Python version

This program will solve all of the problems presented by the Advent of Code 20{year} which can be found at <https://adventofcode.com/20{year}>

Each day code script will output the answer to each puzzle into the console with a label to identify what puzzle the solution is for.

The AocYEAR_SolveAll.py script will use the day code scripts and reroute the outputs into a text file
    '''
    f.write(readme_str)
    f.close()


def create_solve_all():
    global year
    f = open(f'aoc_{year}_solve_all.py', 'w+')
    solve_all_str = f'''from aoc_{year}_day_code import day_01,day_02,day_03,day_04,day_05,day_06,day_07,day_08,day_09,day_10,day_11,day_12,day_13,day_14,day_15,day_16,day_17,day_18,day_19,day_20,day_21,day_22,day_23,day_24,day_25
import sys, io

def solve_all():
    out = io.StringIO.StringIO()
    sys.stdout = out

    day_01.solve()
    day_02.solve()
    day_03.solve()
    day_04.solve()
    day_05.solve()
    day_06.solve()
    day_07.solve()
    day_08.solve()
    day_09.solve()
    day_10.solve()
    day_11.solve()
    day_12.solve()
    day_13.solve()
    day_14.solve()
    day_15.solve()
    day_16.solve()
    day_17.solve()
    day_18.solve()
    day_19.solve()
    day_20.solve()
    day_21.solve()
    day_22.solve()
    day_23.solve()
    day_24.solve()
    day_25.solve()

    file = open("aoc{year}_puzzle_solutions.txt", "w+")
    for l in out.buflist:
        file.write(l)
    file.close()
    '''
    f.write(solve_all_str)
    f.close()


def create_input_files():
    global year
    input_dir = 'inputs'
    os.mkdir(input_dir)
    os.chdir(input_dir)

    for i in range(1, 26):
        f = open(f'day{i:02}.txt', 'w+')
        f.write(f'AOC{year}_INPUT_DAY{i:02}')
        f.close()

    os.chdir('..')


def create_day_code():
    global year
    day_code_dir = f'aoc_{year}_day_code'
    os.mkdir(day_code_dir)
    os.chdir(day_code_dir)

    create_init_py()

    for i in range(1, 26):
        f = open(f'day_{i:02}.py', 'w+')
        day_code_str = f'''import os

def solve():
    file_loc = "inputs/day{i:02}.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location: str):
    if os.path.exists(file_location):
        file = open(file_location)
        f = file.readline().strip()
        if not f == 'AOC{year}_INPUT_DAY{i:02}':
            print("Invalid input file header: Day{i:02}")
            return False
     
        return file.read()
    else:
        print("Day {i:02} input file does not exist")

def solve_puzzle_1(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    output = 0

    print("Day {i:02} Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location: str):
    inputs = load_inputs(file_location)
    if inputs == '':
        return

    output = 0

    print("Day({i:02} Puzzle 2 Solution - " + str(output))
    '''
        f.write(day_code_str)
        f.close()

    os.chdir('..')


year = sys.argv[1]

top_dir_path = 'AOC'+year

os.mkdir(top_dir_path)
os.chdir(top_dir_path)

create_init_py()
create_gitignore()
create_main()
create_solve_all()
create_input_files()
create_day_code()
