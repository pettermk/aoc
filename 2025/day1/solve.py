from functools import reduce


def read_input():
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
        lines = f.read().split('\n')
        lines.pop()
    return lines

def main():
    data = read_input()
    count = 0
    position = 50
    for line in data:
        print(line)
        distance = int(line[1:])
        if line[0] == 'R':
            position = (position + distance)
            if position >= 100:
                count = count + 1 + (distance // 100)
        else:
            position = position - distance
            if position <= 0:
                count = count + 1 + (distance // 100)
                if position == -distance:
                    count = count - 1
            position = position + 100
        position = position % 100
        print(position)
        print(count)

def part2():
    data = read_input()
    state: list[int] = [50, 0]
    def turn(state: list[int], direction: str) -> list[int]:
        if direction == 'R':
            state[0] = state[0] + 1
            if state[0] == 100:
                state[0] = 0
                state[1] = state[1] + 1
        else:
            state[0] = state[0] - 1
            if state[0] == 0:
                state[1] = state[1] + 1
            if state[0] == - 1:
                state[0] = 99
        return state

    for line in data:
        for _ in range(int(line[1:])):
            state = turn(state, line[0])
    print(state)



if __name__ == '__main__':
    # main()
    part2()
