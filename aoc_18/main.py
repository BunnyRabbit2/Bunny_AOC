"""Main file for Advent of Code 2018"""
from aoc_18_day_code import *
import aoc_18_solve_all
import os

def main():
    """Main entry point for the solving file"""
    print("Starting Advent of Code 2018 program - Python 3 Version")
    os.chdir('aoc_18')
    day_01.solve()
    # aoc_18_solve_all.solve_all()

if __name__ == "__main__":
    main()
    