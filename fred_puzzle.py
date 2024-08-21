# # Three fellows accused of stealing CDs make the following statements:
# #  (1) Ed: “Fred did it, and Ted is innocent”.
# #  (2) Fred: “If Ed is guilty, then so is Ted”.
# #  (3) Ted: “’Im innocent, but at least one of the others is guilty”.
#  Let us write the following propositions:
#  Fg means Fred is guilty, and Fi means Fred is innocent, Tg and Ti for Ted and Eg and
#  Ei for Ed.
#  1. Ed says: Fg ∧ Ti
#  2. Fred says: Eg → Tg
#  3. Ted says: Ti ∧ (Fg ∨ Eg)
#  We know that the guilty is lying and the innocent tells the truth.


from z3 import *
fg, fi, tg, ti, eg, ei = Bools('fg fi tg ti eg ei')
s=Solver()
s.add(fg!=fi)
s.add(tg!=ti)
s.add(eg!=ei)
s.add(ei==And(fg, ti))
s.add(fi==Implies(eg, tg))
#s.add(fi==Or(Not(eg), tg)) # Or(-x, y) is the same as Implies
s.add(ti==And(ti, Or(fg, eg)))
print (s.check())
print (s.model())