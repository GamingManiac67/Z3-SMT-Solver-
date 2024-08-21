from z3 import *
# 0- weight absent, 1- on left pan, 2- on right pan:
w1, w3, w9, obj = Ints('w1 w3 w9 obj')
obj_w = Int('obj_w')
s=Solver()
s.add(And(w1>=0, w1<=2))
s.add(And(w3>=0, w3<=2))
s.add(And(w9>=0, w9<=2))
# object is always on left or right pan:
s.add(And(obj>=1, obj<=2))
# object must weight something:
s.add(obj_w>0)
left, right = Ints('left right')
# left pan is a sum of weights/object, if they are present on pan:
s.add(left == If(w1==1, 1, 0) + If(w3==1, 3, 0) + If(w9==1, 9, 0) + If(obj==1, obj_w, 0))
# same for right pan:
s.add(right == If(w1==2, 1, 0) + If(w3==2, 3, 0) + If(w9==2, 9, 0) + If(obj==2, obj_w, 0))
# both pans must weight something:
s.add(left>0)
s.add(right>0)
# pans must have equal weights:
s.add(left==right)
# get all results:
results=[]
while True:
    if s.check() == sat:
        m = s.model()
        #print m
        print("left: ", end=' ')
        print("w1" if m[w1].as_long()==1 else " ", end=' '),
        print("w3" if m[w3].as_long()==1 else " ", end=' '),
        print("w9" if m[w9].as_long()==1 else " ", end=' '),
        print(("obj_w=%2d" % m[obj_w].as_long()) if m[obj].as_long()==1 else "", end=' '),
        print(" | right: ", end=' '),
        print("w1" if m[w1].as_long()==2 else " ", end=' '),
        print("w3" if m[w3].as_long()==2 else " ", end=' '),
        print("w9" if m[w9].as_long()==2 else " ", end=' '),
        print(("obj_w=%2d" % m[obj_w].as_long()) if m[obj].as_long()==2 else ""),
        print("", end=' ')
        results.append(m)
        block = []
        for d in m:
        # skip internal variables, do not add them to blocking constraint:
            if str(d).startswith ("z3name"):
                continue
            c=d()
            block.append(c != m[d])
        s.add(Or(block))
    else:
        print("total results", len(results))
        break