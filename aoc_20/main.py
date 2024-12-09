"""Main file for Advent of Code 2020"""
from aoc_20_day_code import *
import aoc_20_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2020 program - Python 3 Version")
    os.chdir('aoc_20')
    day_01.solve()
    # aoc_20_solve_all.solve_all()

if __name__ == "__main__":
    main()
    