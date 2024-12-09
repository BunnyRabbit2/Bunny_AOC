"""Will solve all puzzles and send output to a text file"""
import io
from contextlib import redirect_stdout
from aoc_24_day_code import *


def solve_all():
    """Solves all of the puzzles"""
    out = io.StringIO()
    
    with redirect_stdout(out):
        day_01.solve()
        day_02.solve()
        day_03.solve()
        day_04.solve()
        day_05.solve()
        day_06.solve()
        day_07.solve()
        day_08.solve()
        day_09.solve()
        day_10.solve()
        day_11.solve()
        day_12.solve()
        day_13.solve()
        day_14.solve()
        day_15.solve()
        day_16.solve()
        day_17.solve()
        day_18.solve()
        day_19.solve()
        day_20.solve()
        day_21.solve()
        day_22.solve()
        day_23.solve()
        day_24.solve()
        day_25.solve()

    solution_file = open("aoc_2024_puzzle_solutions.txt", "w+")
    for line in out.getvalue():
        solution_file.write(line)
    solution_file.close()
    