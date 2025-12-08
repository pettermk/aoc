from functools import reduce

def read_input():
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
        lines = f.readlines()
        return map(lambda x: [int(y) for y in x.rstrip().split(',')], lines)

def part1():
    data = list(read_input())

    distances: list[tuple[tuple[int, int], int]] = []
    for i in range(0, len(data)):
        for j in range(0, i):
            if i == j:
                continue
            distances.append(((i,j),sum((x[0]-x[1])**2 for x in zip(data[i], data[j])) ** (1/2)))
    distances = sorted(distances, key=lambda x: x[1])
    circuits: list[list[int]] = [[a] for a in range(0, len(data))]
    for distance in distances[0:1000]:
        b1, b2 = distance[0]
        if any(b1 in l and b2 in l for l in circuits):
            continue
        first = next(c for c in circuits if b1 in c)
        second = next(c for c in circuits if b2 in c)
        circuits.pop(circuits.index(second))
        circuits[circuits.index(first)] = list(set().union(first, second))
    c = reversed(sorted(circuits, key=lambda x: len(x)))
    c = [len(x) for x in c]
    print(reduce(lambda x, y: x * y, c[0:3], 1))

    # print(circuits)

def part2():
    data = list(read_input())

    distances: list[tuple[tuple[int, int], int]] = []
    for i in range(0, len(data)):
        for j in range(0, i):
            if i == j:
                continue
            distances.append(((i,j),sum((x[0]-x[1])**2 for x in zip(data[i], data[j])) ** (1/2)))
    distances = sorted(distances, key=lambda x: x[1])
    circuits: list[list[int]] = [[a] for a in range(0, len(data))]
    for distance in distances:
        b1, b2 = distance[0]
        if any(b1 in l and b2 in l for l in circuits):
            continue
        first = next(c for c in circuits if b1 in c)
        second = next(c for c in circuits if b2 in c)
        circuits.pop(circuits.index(second))
        circuits[circuits.index(first)] = list(set().union(first, second))
        if len(circuits) == 1:
            print(data[b1][0] * data[b2][0])
            break

if __name__ == '__main__':
    part2()
