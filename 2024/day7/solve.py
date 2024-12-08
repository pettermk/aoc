from functools import cache
from itertools import product, pairwise

with open('input.txt') as f:
    input = []
    for line in f.readlines():
        eq = line.rstrip('\n').split(': ')
        left = int(eq[0])
        nums = [int(n) for n in eq[1].split(' ')]
        input.append((left, nums))


    sum = 0
    operations = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '||': lambda x, y: int(str(x) + str(y)),
    }
    print(input)
    correct_eqs = []
    s = 0
    for eq in input:
        nums = eq[1]
        answer = eq[0]
        combs = list(product(['+', '*', '||'], repeat=len(nums) - 1))
        for comb in combs:
            start = nums[0]
            for partial in zip(pairwise(nums), comb):
                start = operations[partial[1]](start, partial[0][1])
                if start > answer:
                    break
            if start == answer:
                correct_eqs.append(eq)
                s += answer
                break
    print(s)
