from aoc_16_day_code import day_01,day_02,day_03,day_04,day_05,day_06,day_07,day_08,day_09,day_10,day_11,day_12,day_13,day_14,day_15,day_16,day_17,day_18,day_19,day_20,day_21,day_22,day_23,day_24,day_25
import sys, io

def solve_all():
    out = io.StringIO.StringIO()
    sys.stdout = out

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

    file = open("aoc16_puzzle_solutions.txt", "w+")
    for l in out.buflist:
        file.write(l)
    file.close()
    