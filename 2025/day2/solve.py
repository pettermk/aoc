from functools import cache
from contextlib import suppress
from itertools import islice, product
from math import isqrt


def read_input() -> str:
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
        lines = f.read()
    return lines


def part1():
    data = read_input().split(',')
    count = 0
    for r in data:
        bounds = r.split('-')
        for i in range(int(bounds[0]), int(bounds[1]) + 1):
            num = str(i)
            length = len(num)
            if length % 2 :
                continue
            middle = length // 2
            if num[middle:] == num[:middle]:
                count = count + i
                print(f'Found hit {num}')
    print(count)

def iter_index(iterable, value, start=0, stop=None):
    "Return indices where a value occurs in a sequence or iterable."
    # iter_index('AABCADEAF', 'A') → 0 1 4 7
    seq_index = getattr(iterable, 'index', None)
    if seq_index is None:
        iterator = islice(iterable, start, stop)
        for i, element in enumerate(iterator, start):
            if element is value or element == value:
                yield i
    else:
        stop = len(iterable) if stop is None else stop
        i = start
        with suppress(ValueError):
            while True:
                yield (i := seq_index(value, i, stop))
                i += 1

def sieve(n):
    "Primes less than n."
    # sieve(30) → 2 3 5 7 11 13 17 19 23 29
    if n > 2:
        yield 2
    data = bytearray((0, 1)) * (n // 2)
    for p in iter_index(data, 1, start=3, stop=isqrt(n) + 1):
        data[p*p : n : p+p] = bytes(len(range(p*p, n, p+p)))
    yield from iter_index(data, 1, start=3)

@cache
def factor_generator(n):
    "Prime factors of n."
    # factor(99) → 3 3 11
    # factor(1_000_000_000_000_007) → 47 59 360620266859
    # factor(1_000_000_000_000_403) → 1000000000000403
    for prime in sieve(isqrt(n) + 1):
        while not n % prime:
            yield prime
            n //= prime
            if n == 1:
                return
    if n > 1:
        yield n

@cache
def factor(n):
    return [f for f in factor_generator(n)]


def part2():
    data = read_input().split(',')
    count = 0
    max_factorials = 0
    for r in data:
        bounds = r.split('-')
        for i in range(int(bounds[0]), int(bounds[1]) + 1):
            num = str(i)
            if len(num) == 1:
                continue
            length = len(num)
            factors = factor(length)
            max_factorials = max(max_factorials, len(factors))
            # print([f for f in factors])
            # print([f for f in product(factors, repeat=len(factors) - 1)])
            test_cases = [(1,length)]
            if len(factors) == 3:
                test_cases.append((factors[0] * factors[1], factors[2]))
                test_cases.append((factors[0], factors[1] * factors[2]))
                test_cases.append((factors[2], factors[0] * factors[1]))
                test_cases.append((factors[1] * factors[2], factors[0]))
            elif len(factors) == 2:
                test_cases.append((factors[0], factors[1]))
                test_cases.append((factors[1], factors[0]))
            elif len(factors) == 1:
                pass
            else:
                print(factors)
                print(test_cases)
                raise Exception(f'Exception at {num}')
            invalid = False
            # print(f'Starting test cases for {num}')
            for test_case in test_cases:
                previous_subs = None
                # print(f'Starting test case {test_case}')
                # print(list(range(0, test_case[0] * (test_case[1]), test_case[0])))
                differed = False
                for j in range(0, test_case[0] * (test_case[1]), test_case[0]):
                    subs = num[j:j+test_case[0]]
                    # print(subs)
                    if previous_subs is not None and subs != previous_subs:
                        # print(f'Previous {previous_subs} was not equal to {subs}, breaking')
                        differed = True
                        break
                    previous_subs = subs
                if not differed:
                    invalid = True
                    break
            if invalid:
                print(f'Number {num} is invalid')
                count = count + i
    print(count)



if __name__ == '__main__':
    part2()


