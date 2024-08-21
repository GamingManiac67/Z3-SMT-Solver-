import z3
from z3 import *
m=BitVec('m', 32)
s=Solver()
# wouldn't work for 10, etc
divisor=3
# random constant, must be divisible by divisor:
const=(0x1234567*divisor)
s.add(const*m == const/divisor)
print(s.check())
print("%x" % s.model()[m].as_long())
print(s.model())