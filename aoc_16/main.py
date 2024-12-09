"""Main file for Advent of Code 2016"""
from aoc_16_day_code import *
import aoc_16_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2016 program - Python 3 Version")
    os.chdir('aoc_16')
    day_01.solve()
    # aoc_16_solve_all.solve_all()

if __name__ == "__main__":
    main()
    