"""Main file for Advent of Code 2022"""
from aoc_22_day_code import *
import aoc_22_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2022 program - Python 3 Version")
    os.chdir('aoc_22')
    day_01.solve()
    # aoc_22_solve_all.solve_all()

if __name__ == "__main__":
    main()
    