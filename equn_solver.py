import z3
from z3 import *
x, y = Reals('x y')
s=Solver()
s.add(x>0)
s.add(y>0)
s.add(x+y == 4*x*y)
print(s.check())
m=s.model()
print("the model:")
print(m)
print("the answer:", m.evaluate (1/x + 1/y))