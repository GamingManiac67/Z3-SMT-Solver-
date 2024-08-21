# min(x,y) = y ⊕((x⊕y)∧(−(x < y)))
# max(x,y) = x⊕((x⊕y)∧(−(x < y)))
import z3
from z3 import *
def floor(x):
    return x&0xff00
def ceiling(x):
    return If((x&0xff)!=0, (x&0xff00)+0x100, x)