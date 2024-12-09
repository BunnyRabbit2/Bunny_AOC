"""Main file for Advent of Code 2019"""
from aoc_19_day_code import *
import aoc_19_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2019 program - Python 3 Version")
    os.chdir('aoc_19')
    day_01.solve()
    # aoc_19_solve_all.solve_all()

if __name__ == "__main__":
    main()
    