from itertools import batched

from numba import njit
from typing import List


def get_input() -> List[int]:
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
        disk:List[int] = []
        input = f.read().rstrip('\n')
    
        for index, pair in enumerate(batched(input, n=2)):
            for _ in range(int(pair[0])):
                disk.append(index)
            if len(pair) == 2:
                for _ in range(int(pair[1])):
                    disk.append(-1)
    return disk

    
disk = get_input()

@njit
def part1(disk: List[int]):
    empties = [i for i, char in enumerate(disk) if char == -1]
    files = [(i, char) for i, char in enumerate(disk) if char != -1]
    
    still_space = True
    while still_space:
        empties = [i for i, char in enumerate(disk) if char == -1]
        files = [(i, char) for i, char in enumerate(disk) if char != -1]
        if files[-1][0] == (empties[0] - 1):
            break
        print(f'swapping {empties[0]} and {files[-1][0]}')
        disk[files[-1][0]], disk[empties[0]] = disk[empties[0]], disk[files[-1][0]]
    return disk

disk = part1(disk)

print(sum([i*int(element) for i, element in enumerate(disk) if element != -1]))

def input_to_str(inp):
    return ''.join([
        str(element[0]) * element[1][0] + '.' * element[1][1]
        for element in inp
    ])
def input_to_checksum(inp):
    sequence = [[element[0]] * element[1][0] + [0] * element[1][1] for element in inp]
    seq = [x for xs in sequence for x in xs]
    b = [i * element for i, element in enumerate(seq)]
    return sum(b)

def part2():
    #with open('input.txt') as f:
    with open('input.txt') as f:
        inp = batched([int(x) for x in f.read().rstrip('\n')], n=2)
        inp = [[i, list(batch)] for i, batch in enumerate(list(inp))]


    search_index = len(inp) - 1
    while search_index > 0:
        candidate = inp[search_index].copy()
        if len(candidate[1]) == 1:
            candidate[1].append(0)
        try:
            index = next((i for i, pair in enumerate(inp[:(search_index)]) if pair[1][1] >= candidate[1][0]))
        except StopIteration:
            search_index -= 1
            continue
        # Replace entire moving entry with zeroes to the previous point
        inp[search_index - 1][1][1] += (inp[search_index][1][0] + inp[search_index][1][1])
        # 
        candidate[1][1] = inp[index][1][1] - candidate[1][0]
        # Remove that free space
        inp[index][1][1] = 0
        del(inp[search_index])
        search_index -= 0
        inp.insert(index + 1, candidate.copy())

    print(input_to_str(inp))
    print(input_to_checksum(inp))

part2()

