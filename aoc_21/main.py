"""Main file for Advent of Code 2021"""
from aoc_21_day_code import *
import aoc_21_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2021 program - Python 3 Version")
    os.chdir('aoc_21')
    day_01.solve()
    # aoc_21_solve_all.solve_all()

if __name__ == "__main__":
    main()
    