import numpy as np

import re

with open('test_input.txt') as f:
    equations = f.read().split('\n\n')
    input: list[tuple[np.ndarray, np.ndarray]] = []
    regex = re.compile(r'[X|Y][\+|=]([0-9]+)')
    for eq in equations:
        eq = eq.split('\n')
        eq.pop()
        matches = regex.match(eq[0]).groups()
        print(matches)
        a = np.array(list(regex.match(eq[0]).groups()))
           
