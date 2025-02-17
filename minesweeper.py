import z3
known=[
 "01?10001?",
 "01?100011",
 "011100000",
 "000000000",
 "111110011",
 "????1001?",
 "????3101?",
 "?????211?",
 "?????????"]
from z3 import *
import sys
WIDTH=len(known[0])
HEIGHT=len(known)
print ("WIDTH=", WIDTH, "HEIGHT=", HEIGHT)
def chk_bomb(row, col):
    s=Solver()
    cells=[[Int('r%d_c%d' % (r,c)) for c in range(WIDTH+2)] for r in range(HEIGHT+2)]
    # make border
    for c in range(WIDTH+2):
        s.add(cells[0][c]==0)
        s.add(cells[HEIGHT+1][c]==0)
    for r in range(HEIGHT+2):
        s.add(cells[r][0]==0)
        s.add(cells[r][WIDTH+1]==0)
    for r in range(1,HEIGHT+1):
        for c in range(1,WIDTH+1):
    # otherwise-1 is possible, etc:
            s.add(Or(cells[r][c]==0, cells[r][c]==1))
            t=known[r-1][c-1]
            if t in "012345678":
                s.add(cells[r][c]==0)
                expr=cells[r-1][c-1] + cells[r-1][c] + cells[r-1][c+1] + cells[r][c-1] + cells[r][c+1] + cells[r+1][c-1] + cells[r+1][c] + cells[r+1][c+1]==int(t)
                if False:
                    print (expr)
                s.add(expr)
    # place bomb:
    s.add(cells[row][col]==1)
    if s.check()==unsat:
        print("row=%d col=%d, unsat!" % (row, col))
# enumerate all hidden cells:
for r in range(1,HEIGHT+1):
    for c in range(1,WIDTH+1):
        if known[r-1][c-1]=="?":
            chk_bomb(r, c)