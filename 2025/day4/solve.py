from os import read


def read_input() -> list[list[str]]:
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
        lines = f.readlines()
    return [
            [c for c in line.rstrip()] for line in lines
            ]
    
directions = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]

def is_within_bounds(x, y, data):
    return x >= 0 and y >= 0 and x < len(data[0]) and y < len(data) 

def can_be_accessed(x, y, data):
    count = 0
    for direction in directions:
        new_position = [x + direction[0], y + direction[1]]
        if is_within_bounds(new_position[0], new_position[1], data) and data[new_position[1]][new_position[0]] != '.':
            count = count + 1
            if count > 3:
                return False
    return True


def part1():
    data = read_input()
    count = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if data[y][x] != '.' and can_be_accessed(x, y, data):
                data[y][x] = 'x'
                count = count + 1
            print(data[y][x], end='')
        print('')
    print(count)


def mark_accessible(data):
    count = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if data[y][x] != '.' and can_be_accessed(x, y, data):
                data[y][x] = 'x'
                count = count + 1
            print(data[y][x], end='')
        print('')


def remove_rolls(data):
    count = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if data[y][x] == 'x':
                data[y][x] = '.'
                count = count + 1
    return count


def part2():
    data = read_input()
    count = 0
    while True:
        mark_accessible(data)
        num_removed = remove_rolls(data)
        if num_removed == 0:
            print(count)
            return
        count = count + num_removed


if __name__ == '__main__':
    part2()

