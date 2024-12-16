import numpy as np

import re

def is_int(number: float):
    return np.isclose(number, np.round(number), 1e-15, 1e-18)

# Part 1
#with open('test_input.txt') as f:
with open('input.txt') as f:
    equations = f.read().split('\n\n')
    r = re.compile(r'[XY][\+=]([0-9]+)', )
    s = 0
    for eq in equations:
        eq = eq.split('\n')
        a = np.array([[int(n) for n in r.findall(eq[0])], [int(n) for n in r.findall(eq[1])]])
        b = np.array([[int(n)] for n in r.findall(eq[2])])

        solution = np.linalg.solve(np.transpose(a),b)

        if all(is_int(n) for n in solution):
            s += solution[0][0] * 3 + solution[1][0] * 1
           
    print(s)

# Part 2
# with open('test_input.txt') as f:
with open('input.txt') as f:
    equations = f.read().split('\n\n')
    r = re.compile(r'[XY][\+=]([0-9]+)', )
    s = 0
    for i, eq in enumerate(equations):
        eq = eq.split('\n')
        a = np.array([[int(n) for n in r.findall(eq[0])], [int(n) for n in r.findall(eq[1])]])
        b = np.array([[int(n) + 10000000000000] for n in r.findall(eq[2])])

        solution = np.linalg.solve(np.transpose(a),b)

        if all(is_int(n) for n in solution):
            s += solution[0][0] * 3 + solution[1][0] * 1
           
    print(s)
