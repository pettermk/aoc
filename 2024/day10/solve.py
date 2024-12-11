from typing import Tuple

def get_input() -> list[list[int]]:
    with open('input.txt') as f:
        input = [line.rstrip('\n') for line in f.readlines()]
        input = [[int(c) for c in line] for line in input]
    return input

        
def get_value(pos: Tuple[int, int], input):
    if pos[1] < len(input) and pos[1] >= 0 and pos[0] < len(input[0]) and pos[0] >= 0:
        return input[pos[1]][pos[0]]
    raise ValueError


search_directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def build_tree_recurse(pos, hits, input):
    try:
        value = get_value(pos, input)
    except ValueError: # Nuthin to see here
        return
    if value == 9:
        hits.append(pos)
        return

    for direction in search_directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        try:
            if get_value(new_pos, input) == value + 1:
                build_tree_recurse(new_pos, hits, input)
        except ValueError: # Nuthin to see here
            pass

def build_tree(pos: Tuple[int, int], input):
    hits: list[Tuple[int, int]] = []

    value = get_value(pos, input)

    for direction in search_directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        try:
            if get_value(new_pos, input) == value + 1:
                build_tree_recurse(new_pos, hits, input)
        except ValueError: # Nuthin to see here
            pass
    return hits


def part1():
    input = get_input()
    width = len(input[0])
    height = len(input)
    sum = 0
    for x in range(width):
        for y in range(height):
            if input[y][x] == 0:
                hits = build_tree((x, y), input)
                sum += len(set(hits))
    print(sum)

part1()
                
def part2():
    input = get_input()
    width = len(input[0])
    height = len(input)
    sum = 0
    for x in range(width):
        for y in range(height):
            if input[y][x] == 0:
                hits = build_tree((x, y), input)
                sum += len(hits)
    print(sum)

part2()
