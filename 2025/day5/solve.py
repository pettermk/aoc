def read_input() -> list[str]:
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
    # with open('synth_input.txt') as f:
        lines = f.read()
        return lines.split('\n\n')

def part1():
    data = read_input()
    ranges = [
            x.split('-') for x in data[0].rsplit()
            ]
    ranges = [
            [int(x[0]), int(x[1])] for x in ranges
            ]

    ranges = list(enumerate(ranges))

    asc = sorted(ranges, key=lambda x: x[1][0])
    desc = sorted(ranges, key=lambda x: x[1][1])
    print(asc)
    print(desc)

    count = 0
    for id_ in data[1].rsplit():
        number = int(id_)
        candidates = filter(lambda x: x[1][0] <= number, asc)
        candidates2 = filter(lambda x: x[1][1] >= number, desc)
        print(number)
        c1 = [x[0] for x in candidates]
        c2 = [x[0] for x in candidates2]
        if set(c1).intersection(set(c2)):
            print(f'Food {number} is fresh')
            count = count + 1
    print(count)

def part2():
    data = read_input()
    ranges = [
            x.split('-') for x in data[0].rsplit()
            ]
    ranges = [
            [int(x[0]), int(x[1])] for x in ranges
            ]
    count = 0
    ranges = sorted(ranges, key=lambda x: x[0])
    x = ranges[0]
    for r in ranges[1:]:
        if r[0] > x[1]:
            count = count + x[1] - x[0] + 1
        else:
            count = count + (r[0] - x[0])
        x = [r[0], max(x[1], r[1])]
    count = count + x[1] - x[0] + 1


if __name__ == '__main__':
    part2()
