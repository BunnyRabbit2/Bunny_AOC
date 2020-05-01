from DayCode import Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day10,Day11,Day12,Day13,Day14,Day15,Day16,Day17,Day18,Day19,Day20,Day21,Day22,Day23,Day24,Day25
import StringIO, sys, io

def SolveAll():
    out = StringIO.StringIO()
    sys.stdout = out

    Day1.solve()
    Day2.solve()
    Day3.solve()
    Day4.solve()
    Day5.solve()
    Day6.solve()
    Day7.solve()
    Day8.solve()
    Day9.solve()
    Day10.solve()
    Day11.solve()
    Day12.solve()
    Day13.solve()
    Day14.solve()
    Day15.solve()
    Day16.solve()
    Day17.solve()
    Day18.solve()
    Day19.solve()
    Day20.solve()
    Day21.solve()
    Day22.solve()
    Day23.solve()
    Day24.solve()
    Day25.solve()

    file = open("puzzle_solutions.txt", "w+")
    for l in out.buflist:
        file.write(l)
    file.close()