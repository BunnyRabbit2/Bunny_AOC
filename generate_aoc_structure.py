"""Used for creation of an Advent of Code folder structure for a year"""
import os
import sys

YEAR = sys.argv[1]

def create_gitignore_file():
    """Creates .gitignore file"""
    gitignore_file = open('.gitignore', 'w+')
    gitignore_file.write('''### Python ###
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
    gitignore_file.close()


def create_main():
    """Creates main file for project"""
    main_file = open('main.py', 'w+')
    main_string = f'''"""Main file for Advent of Code 20{YEAR}"""
from aoc_{YEAR}_day_code import *
import aoc_{YEAR}_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 20{YEAR} program - Python 3 Version")
    os.chdir('aoc_{YEAR}')
    day_01.solve()
    # aoc_{YEAR}_solve_all.solve_all()

if __name__ == "__main__":
    main()
    '''
    main_file.write(main_string)
    main_file.close()


def create_readme():
    """Creates the readme for the project"""
    readme_file = open('README.md', 'w+')
    readme_string = f'''# BunnyAoC20{YEAR} Python 3 version

This program will solve all of the problems presented by the Advent of Code 20{YEAR} which can be found at <https://adventofcode.com/20{YEAR}>

Each day code script will output the answer to each puzzle into the console with a label to identify what puzzle the solution is for.

The aoc_{YEAR}_solve_all.py script will use the day code scripts and reroute the outputs into a text file
    '''
    readme_file.write(readme_string)
    readme_file.close()


def create_solve_all():
    """Creates a script to solve all the puzzles at once"""
    global year
    solve_all_file = open(f'aoc_{YEAR}_solve_all.py', 'w+')
    solve_all_string = f'''"""Will solve all puzzles and send output to a text file"""
import io
from contextlib import redirect_stdout
from aoc_{YEAR}_day_code import *


def solve_all():
    """Solves all of the puzzles"""
    out = io.StringIO()
    
    with redirect_stdout(out):
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

    solution_file = open("aoc_20{YEAR}_puzzle_solutions.txt", "w+")
    for line in out.getvalue():
        solution_file.write(line)
    solution_file.close()
    '''
    solve_all_file.write(solve_all_string)
    solve_all_file.close()


def create_input_files():
    """Creates all input files"""
    input_dir = 'inputs'
    os.mkdir(input_dir)
    os.chdir(input_dir)

    for i in range(1, 26):
        input_file = open(f'day{i:02}.txt', 'w+')
        input_file.write(f'AOC{YEAR}_INPUT_DAY{i:02}')
        input_file.close()

    os.chdir('..')

def create_init_file(day_code = False):
    """Creates an __init__ file"""
    """Creates the init.py file"""
    init_file = open('__init__.py', 'w+')
    if day_code:
        init_file.write("__all__ = ['day_01', 'day_02', 'day_03', 'day_04', 'day_05', 'day_06', 'day_07', 'day_08', 'day_09', 'day_10', 'day_11', 'day_12', 'day_13', 'day_14', 'day_15', 'day_16', 'day_17', 'day_18', 'day_19', 'day_20', 'day_21', 'day_22', 'day_23', 'day_24', 'day_25']")
    init_file.close()

def create_day_code():
    """Creates starting day code for all days"""
    daycode_dir = f'aoc_{YEAR}_day_code'
    os.mkdir(daycode_dir)
    os.chdir(daycode_dir)

    create_init_file(True)

    for i in range(1, 26):
        file_num = f'{i:02}'

        day_code_file = open(f'day_{i:02}.py', 'w+')
        daycode_string = f'''"""Code to solve puzzle for day {file_num}"""
import os

def solve():
    """Solves the day"""
    file_loc = "inputs/day{file_num}.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC{YEAR}_INPUT_DAY{file_num}':
            print("Invalid input file header: Day{file_num}")
            return ''
     
        return input_file.read()
    else:
        print("Day {file_num} input file does not exist")
        return ''

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day {file_num} Puzzle 1 - NO INPUTS")
    else:
        output = 0

        print("Day {file_num} Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day {file_num} Puzzle 2 - NO INPUTS")
    else:
        output = 0

        print("Day {file_num} Puzzle 2 Solution - " + str(output))
    '''
        day_code_file.write(daycode_string)
        day_code_file.close()

    os.chdir('..')

top_dir_p = f'aoc_{YEAR}'

os.mkdir(top_dir_p)
os.chdir(top_dir_p)

create_init_file()
create_gitignore_file()
create_main()
create_solve_all()
create_input_files()
create_day_code()