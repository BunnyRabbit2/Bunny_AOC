"""Main file for Advent of Code 2023"""
from aoc_23_day_code import *
import aoc_23_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2023 program - Python 3 Version")
    os.chdir('aoc_23')
    day_01.solve()
    # aoc_23_solve_all.solve_all()

if __name__ == "__main__":
    main()
    