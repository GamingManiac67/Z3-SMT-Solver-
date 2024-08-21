import z3
from z3 import *

set = [-8, -3, -2, 5, 8]
set_len = len(set)
vars = [Int(f'vars_{i}') for i in range(set_len)]
s = Solver()

rt = [vars[i] * set[i] for i in range(set_len)]
for i in range(set_len):
    s.add(Or(vars[i] == 0, vars[i] == 1))

s.add(sum(rt) == 0)
s.add(sum(vars) >= 1)

def print_solution(m):
    solution = []
    for i in range(set_len):
        if m[vars[i]].as_long() == 1:
            solution.append(set[i])
    print(solution)
    return solution

solutions = []
while s.check() == sat:
    m = s.model()
    solutions.append(print_solution(m))
    
    block = []
    for i in range(set_len):
        block.append(vars[i] != m[vars[i]])
    
    s.add(Or(block))

if not solutions:
    print("No solutions found.")

print(m)
print(solutions)
