import z3
from z3 import *
def func(a):
    return a*1024
a32, out32 = BitVecs('a32 out32', 32)
out32_extended = BitVec('out32_extended', 64)
a64, out64 = BitVecs('a64 out64', 64)
#s=Solver()
s=Optimize()
s.add(out32==func(a32))
s.add(out64==func(a64))
s.add(a64==SignExt(32, a32))
s.add(out32_extended==SignExt(32, out32))
s.add(out64!=out32_extended)
s.minimize(a32)
if s.check()==unsat:
    print ("unsat: everything is OK")
    exit(0)
m=s.model()

def toSigned32(n):
    n = n & 0xffffffff
    return n | (-(n & 0x80000000))
def toSigned64(n):
    n = n & 0xffffffffffffffff
    return n | (-(n & 0x8000000000000000))
print ("a32=0x%x or %d" % (m[a32].as_long(), toSigned32(m[a32].as_long())))
print ("out32=0x%x or %d" % (m[out32].as_long(), toSigned32(m[out32].as_long())))
print ("out32_extended=0x%x or %d" % (m[out32_extended].as_long(), toSigned64(m[
out32_extended].as_long())))
print ("a64=0x%x or %d" % (m[a64].as_long(), toSigned64(m[a64].as_long())))
print ("out64=0x%x or %d" % (m[out64].as_long(), toSigned64(m[out64].as_long())))

#  s.add(a32<100)
#  Then below is the case for unsat
#  a32=0x80000000 or-2147483648
#  out32=0x0 or 0
#  out32_extended=0x0 or 0
#  a64=0xffffffff80000000 or-2147483648
#  out64=0xfffffe0000000000 or-2199023255552
# IF s.add(a32>0) then no error will come



# # Absolute Function
#  def func(a):
#       return If(a<0,-a, a)
#  a32=0x80000000 or-2147483648
#  out32=0x80000000 or-2147483648
#  out32_extended=0xffffffff80000000 or-2147483648
#  a64=0xffffffff80000000 or-2147483648
#  out64=0x80000000 or 2147483648
#  This is INT_MIN, and-INT_MIN == INT_MIN

