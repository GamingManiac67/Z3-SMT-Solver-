import z3
from z3 import *
def func(a,b):
    return a+b
a32, b32, out32 = BitVecs('a32 b32 out32', 32)
out32_extended = BitVec('out32_extended', 64)
a64, b64, out64 = BitVecs('a64 b64 out64', 64)
s=Optimize()
s.add(out32==func(a32, b32))
s.add(out64==func(a64, b64))
s.add(a64==SignExt(32, a32))
s.add(b64==SignExt(32, b32))
s.add(out32_extended==SignExt(32, out32))
s.add(out64!=out32_extended)
s.minimize(a32)
s.minimize(b32)
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
print ("b32=0x%x or %d" % (m[b32].as_long(), toSigned32(m[b32].as_long())))
print ("out32=0x%x or %d" % (m[out32].as_long(), toSigned32(m[out32].as_long())))
print ("out32_extended=0x%x or %d" % (m[out32_extended].as_long(), toSigned64(m[out32_extended].as_long())))
print ("a64=0x%x or %d" % (m[a64].as_long(), toSigned64(m[a64].as_long())))
print ("b64=0x%x or %d" % (m[b64].as_long(), toSigned64(m[b64].as_long())))
print ("out64=0x%x or %d" % (m[out64].as_long(), toSigned64(m[out64].as_long())))

# Exlpains abt Overflow
# a32=0x1 or 1
# b32=0x7fffffff or 2147483647
# out32=0x80000000 or -2147483648
# out32_extended=0xffffffff80000000 or -2147483648
# a64=0x1 or 1
# b64=0x7fffffff or 2147483647
# out64=0x80000000 or 2147483648
