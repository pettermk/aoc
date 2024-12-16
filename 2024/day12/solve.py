from typing import Tuple


def get_input() -> list[list[str]]:
    with open('input.txt') as f:
        input = [line.rstrip('\n') for line in f.readlines()]
        input = [l for l in input]
    return input

        
def get_value(pos: Tuple[int, int], input) -> str:
    if pos[1] < len(input) and pos[1] >= 0 and pos[0] < len(input[0]) and pos[0] >= 0:
        return input[pos[1]][pos[0]]
    raise ValueError


search_directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def build_tree_recurse(pos, positions, input):
    try:
        value = get_value(pos, input)
    except ValueError: # Nuthin to see here
        return

    positions.append(pos)
    for direction in search_directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos in positions:
            continue
        try:
            if get_value(new_pos, input) == value:
                build_tree_recurse(new_pos, positions, input)
        except ValueError: # Nuthin to see here
            pass

def build_tree(pos: Tuple[int, int], input):
    positions: list[Tuple[int, int]] = []

    value = get_value(pos, input)

    positions.append(pos)
    for direction in search_directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos in positions:
            continue
        try:
            if get_value(new_pos, input) == value:
                build_tree_recurse(new_pos, positions, input)
        except ValueError: # Nuthin to see here
            pass
    return {
        'positions': positions,
        'value': value
    }

input = get_input()
regions = []
visited_positions = set()
for i in range(len(input[0])):
    for j in range(len(input)):
        if (i, j) not in visited_positions:
            region = build_tree((i, j), input)
            regions.append(region)
            visited_positions.update(region["positions"])

print(regions)

total_prices = 0
for region in regions:
    fences = 0
    for pos in region['positions']:
        for direction in search_directions:
            try:
                if get_value((pos[0] + direction[0], pos[1] + direction[1]), input) != get_value(pos, input):
                    fences += 1
            except ValueError:
                fences +=1

    print(f'Region {region["value"]} price {len(region["positions"]) * fences}')
    total_prices += len(region["positions"]) * fences

print(total_prices)
