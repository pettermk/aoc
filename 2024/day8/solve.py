from itertools import combinations
from typing import List, Tuple, Dict, Set


def get_char(x:int, y: int, input: List[str]) -> str:
    return input[y][x]


def get_input() -> Dict[str, List[Tuple[int, int]]]:
    with open('input.txt') as f:
        # with open('test_input.txt') as f:
        input = [line.rstrip('\n') for line in f.readlines()]
    
        positions: Dict[str, List[Tuple[int, int]]] = {}
        for i, line in enumerate(input):
            for j, letter in enumerate(line):
                if letter != '.':
                    if letter in positions:
                        positions[letter].append((j, i))
                    else:
                        positions[letter] = [(j, i)]
        print(positions)
        return positions

def is_within_bounds(x, y) -> bool:
    with open('input.txt') as f:
        # with open('test_input.txt') as f:
        ip = [line.rstrip('\n') for line in f.readlines()]

    return x < len(ip[0]) and x >= 0 and y < len(ip) and y >= 0


# Part 1
input = get_input()

antinodes: Set[Tuple[int, int]] = set()
for letter, positions in input.items():
    pairs = list(combinations(positions, 2))
    for pair in pairs:
        diff = tuple(x - y for x,y in zip(pair[1], pair[0]))
        antinodes.add(tuple(x - y for x,y in zip(pair[0], diff)))
        antinodes.add(tuple(x + y for x,y in zip(pair[1], diff)))

an = [x for x in antinodes if is_within_bounds(x [0], x[1])]
print(an)
print(len(an))
        

# Part 2
input = get_input()

antinodes: Set[Tuple[int, int]] = set()
for letter, positions in input.items():
    pairs = list(combinations(positions, 2))
    for pair in pairs:
        diff = tuple(x - y for x,y in zip(pair[1], pair[0]))
        # Subtract
        antinode: Tuple[int, int] = tuple(x - y for x,y in zip(pair[1], diff))
        while is_within_bounds(antinode[0], antinode[1]):
            antinodes.add(antinode)
            antinode = tuple(x - y for x,y in zip(antinode, diff))

        antinode = tuple(x + y for x,y in zip(pair[0], diff))
        while is_within_bounds(antinode[0], antinode[1]):
            antinodes.add(antinode)
            antinode = tuple(x + y for x,y in zip(antinode, diff))

an = [x for x in antinodes if is_within_bounds(x [0], x[1])]
print(an)
print(len(an))
