from __future__ import annotations

# def read_input():
#     # with open('input.txt') as f:
#     with open('test_input.txt') as f:
#         lines = f.readlines()
#         return lines

def read_input() -> list[list[str]]:
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
        lines = f.readlines()
    return [
            [c for c in line.rstrip()] for line in lines
            ]

class Beam():
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def advance(self, data) -> None | Beam:
        self.y = self.y + 1
        if data[self.y][self.x] == '^':
            if data[self.y][self.x - 1] == '|':
                if data[self.y][self.x + 1] == '|':
                self.x = self.x - 1
            return Beam(self.x + 2, self.y)
        return None


def part1():
    data = read_input()
    init_pos = data[0].find('S')
    beams = [Beam(0, init_pos)]
    for i, line in enumerate(data[1:], 1):
        for beam in beams:
            new_beam = beam.advance(data)
            if new_beam is not None:

            data[i][beam.x] = '|'



if __name__ == '__main__':
    part1()
