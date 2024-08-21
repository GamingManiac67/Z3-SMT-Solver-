# The positive integers x1,x2,...,x7 satisfy x6 = 144 and xn+3 = xn+2(xn+1 + xn) for n = 1,2,3,4.
# Find the last three digits of x7

from z3 import *
s=Solver()
x1, x2, x3, x4, x5, x6, x7=Ints('x1 x2 x3 x4 x5 x6 x7')
s.add(x1>=0)
s.add(x2>=0)
s.add(x3>=0)
s.add(x4>=0)
s.add(x5>=0)
s.add(x6>=0)
s.add(x7>=0)
s.add(x6==144)
s.add(x4==x3*(x2+x1))
s.add(x5==x4*(x3+x2))
s.add(x6==x5*(x4+x3))
s.add(x7==x6*(x5+x4))
# get all results:
results=[]
while True:
    if s.check() == sat:
        m = s.model()
        print(m)
        results.append(m)
        block = []
        for d in m:
            c=d()
            block.append(c != m[d])
        s.add(Or(block))
    else:
        print("total results", len(results))
        break