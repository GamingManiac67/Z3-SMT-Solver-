# XOR optimisation: (((y & x)*-2) + (y + x))
import z3
# from z3 import *
# x = BitVec('x', 32)
# y = BitVec('y', 32)
# output = BitVec('output', 32)
# s = Solver()
# s.add(x^y==output)
# s.add(((y & x)*0xFFFFFFFE) + (y + x)!=output)
# print(s.check())


from z3 import *
x = BitVec('x', 64)
y = BitVec('y', 64)
output = BitVec('output', 64)
s = Solver()
s.add(x^y==output)
s.add((x + y- ((x & y)<<1)) != output)
print(s.check())

# IN both codes ((x & y)<<1) and (y & x)*0xFFFFFFFE) are doing the same
# First of all, binary addition can be viewed as binary XORing with carrying (2.3.2). Here is an example: let’s add 2
#  (10b) and 2 (10b). XORing these two values resulting 0, but there is a carry generated during addition of two second
#  bits. That carry bit is propagated further and settles at the place of the 3rd bit: 100b. 4 (100b) is hence a final result
#  of addition.
#  If the carry bits are not generated during addition, the addition operation is merely XORing. For example, let’s
#  add 1 (1b) and 2 (10b). 1+2 equals to 3, but 1⊕2 is also 3.
#  If the addition is XORing plus carry generation and application, we should eliminate effect of carrying somehow
#  here. The first part of the expression (x+y) is addition, the second ((x&y) << 1) is just calculation of every carry bit
#  which was used during addition. If to subtract carry bits from the result of addition, the only XOR effect is left then.

# Average Algo
#and r1,ry,rx
#xor r2,ry,rx
#shrs r3,r2,1
#add r4,r3,r1
#Expr: (((y ^ x) >>s 1) + (y & x))