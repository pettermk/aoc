import re
from functools import reduce
from itertools import pairwise

def read_input():
    # with open('input.txt') as f:
    with open('test_input.txt') as f:
        lines = f.readlines()
        return map(lambda x: re.split(r'\s+', x.strip()), lines)

def read_input2():
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
        return f.readlines()

def part1():
    data = list(read_input())
    operations = data.pop()
    data = [[int(s) for s in line] for line in data]
    solutions = data.pop(0)
    functions = {
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
            }
    for i, start in enumerate(solutions):
        column = [j[i] for j in data]
        solutions[i] = reduce(functions[operations[i]], column, start)
    print(sum(solutions))

def part2():
    data = list(read_input2())
    operations = data.pop().rstrip()
    indices = [i for i,c in enumerate(operations) if c != ' ' ]
    indices.append(max([len(o) for o in data]))
    count = 0
    functions = {
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
            }
    for start, end in pairwise(indices):
        numbers = []
        for i in range(end - 2, start - 1, -1):
            digits = []
            for line in data:
                if line[i] != ' ':
                    digits.append(line[i])
            numbers.append(digits)
        numbers = [int(''.join(number)) for number in numbers]
        count = count + reduce(functions[operations[start]], numbers[1:], numbers[0])
        print(numbers)
    print(count)

if __name__ == '__main__':
    part2()
