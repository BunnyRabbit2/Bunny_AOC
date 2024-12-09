"""Main file for Advent of Code 2015"""
from aoc_15_day_code import *
import aoc_15_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2015 program - Python 3 Version")
    os.chdir('aoc_15')
    # day_18.solve()
    aoc_15_solve_all.solve_all()

if __name__ == "__main__":
    main()
    