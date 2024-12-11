from functools import cache
import random


def get_input() -> list[int]:
    with open('input.txt') as f:
        input = [int(x) for x in f.readline().rstrip('\n').split(' ')]
    return input

input = get_input()


@cache
def process_stone(stone: int, generation: int, stop_condition: int):
    if (random.randint(0,10000) == 0):
        print(generation)
    if generation == stop_condition:
        return 1
    if stone == 0:
        return process_stone(1, generation + 1, stop_condition)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        l = int(len(s) / 2)
        return process_stone(int(s[:l]), generation + 1, stop_condition) \
            + process_stone(int(s[l:]), generation + 1, stop_condition)
    else:
        return process_stone(2024* stone, generation + 1, stop_condition)

def part1(input: list[int]):
    for j in range(25):
        print(j)
        print(len(input))
        i = 0
        while i < len(input):
            if input[i] == 0:
                input[i] = 1
                i += 1
            elif len(str(input[i])) % 2 == 0:
                s = str(input[i])
                l = int(len(s) / 2)
                input[i] = int(s[:l])
                input.insert(i+1, int(s[l:]))
                i += 2
            else:
                input[i] = 2024 * input[i]
                i += 1
    print(len(input))
    
# part1(input)

def part2(input: list[int]):
    total = 0
    for stone in input:
        stop_condition = 75
        generation = 0
        total += process_stone(stone, generation, stop_condition)
    print(total)

part2(input)
