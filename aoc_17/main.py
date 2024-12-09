"""Main file for Advent of Code 2017"""
from aoc_17_day_code import *
import aoc_17_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2017 program - Python 3 Version")
    os.chdir('aoc_17')
    day_01.solve()
    # aoc_17_solve_all.solve_all()

if __name__ == "__main__":
    main()
    