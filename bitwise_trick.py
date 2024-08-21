import z3
from z3 import *
s=Solver()
a, b=BitVecs('a b', 5)
x, y=BitVecs('x y', 5)
s.add(ForAll(x, ForAll(y, ((x+a)^b)-a == ((x-a)^b)+a )))
# enumerate all possible solutions:
results=[]
while True:
    if s.check() == sat:
        m = s.model()
        print (m)
        results.append(m)
        block = []
        for d in m:
            c=d()
            block.append(c != m[d])
            s.add(Or(block))
    else:
        print("results total=", len(results))
        break