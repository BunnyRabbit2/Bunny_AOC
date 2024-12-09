"""Main file for Advent of Code 2024"""
from aoc_24_day_code import *
import aoc_24_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2024 program - Python 3 Version")
    os.chdir('aoc_24')
    day_02.solve()
    # aoc_24_solve_all.solve_all()

if __name__ == "__main__":
    main()
    