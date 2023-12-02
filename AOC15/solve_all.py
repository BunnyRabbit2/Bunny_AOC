from day_code import day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8, day_9, day_10, day_11, day_12, day_13, day_14, day_15, day_16, day_17, day_18, day_19, day_20, day_21, day_22, day_23, day_24, day_25
import sys
from io import StringIO


def solve_all():
    out = StringIO()
    sys.stdout = out

    day_1.solve()
    day_2.solve()
    day_3.solve()
    day_4.solve()
    day_5.solve()
    day_6.solve()
    day_7.solve()
    day_8.solve()
    day_9.solve()
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

    file = open("puzzle_solutions.txt", "w+")
    for l in out.buflist:
        file.write(l)
    file.close()
