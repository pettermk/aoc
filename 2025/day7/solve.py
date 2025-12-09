from __future__ import annotations
from re import X
from time import sleep

import numba

# def read_input():
#     # with open('input.txt') as f:
#     with open('test_input.txt') as f:
#         lines = f.readlines()
#         return lines

def read_input() -> list[list[str]]:
    # with open('input.txt') as f:
    with open('test_input.txt') as f:
        lines = f.readlines()
    return [
            [c for c in line.rstrip()] for line in lines
            ]

class Counter():
    i: int = 0
    added_nodes: list[tuple[int, int]] = []

    @staticmethod
    def increment():
        Counter.i = Counter.i + 1

    @staticmethod
    def get_count():
        return Counter.i

    @staticmethod
    def add_node(node):
        Counter.added_nodes.append(node)

    @staticmethod
    def node_exists(node):
        return node in Counter.added_nodes

class Beam():
    x: int
    y: int
    destruct: bool = False

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def advance(self, data) -> None | Beam:
        self.y = self.y + 1
        if data[self.y][self.x] == '^':
            if data[self.y][self.x - 1] == '|':
                if data[self.y][self.x + 1] == '|':
                    self.destruct = True
                    return None
                else:
                    self.x = self.x + 1
                    Counter.increment()
                    return None
            else:
                Counter.increment()
                self.x = self.x - 1
                if data[self.y][self.x + 1] == '|':
                    return None
                else:
                    return Beam(self.x + 2, self.y)

def part1():
    data = read_input()
    init_pos = data[0].index('S')
    beams = [Beam(init_pos, 0)]
    for i, line in enumerate(data[1:], 1):
        beams = sorted(beams, key=lambda x: x.x)
        for beam in beams.copy():
            new_beam = beam.advance(data)
            if beam.destruct:
                beams.pop(beams.index(beam))
                continue
            if new_beam is not None:
                beams.append(new_beam)
                data[i][new_beam.x] = '|'

            data[i][beam.x] = '|'
        print('\n'.join(''.join(s) for s in data))
    print(Counter.get_count())

class Node():
    left: Node | None
    right: Node | None
    parent: Node | None
    x: int
    y: int

    def __init__(self, x, y, parent: Node | None) -> None:
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.parent = parent

    def attach_left(self, node: Node):
        self.left = node
        
    def attach_right(self, node: Node):
        self.right = node

    def traverse(self):
        if self.right is None and self.left is None:
            Counter.increment()
            Counter.increment()
        if self.right:
            self.right.traverse()
        else:
            Counter.increment()
        if self.left:
            self.left.traverse()
        else:
            Counter.increment()



def populate(node: Node, data):
    has_child = False
    for i in range(node.y + 2, len(data), 2):
        if data[i][node.x - 1] == '^':
            if Counter.node_exists((node.x - 1, i)):
                break
            Counter.add_node((node.x - 1, i))
            new_node = Node(node.x - 1, i, None)
            node.attach_left(new_node)
            populate(new_node, data)
            has_child = True
            break
    if not has_child:
        Counter.increment()
    has_child = False
    for i in range(node.y + 2, len(data), 2):
        if data[i][node.x + 1] == '^':
            if Counter.node_exists((node.x + 1, i)):
                break
            Counter.add_node((node.x + 1, i))
            new_node = Node(node.x + 1, i, None)
            node.attach_right(new_node)
            populate(new_node, data)
            has_child = True
            break
    if not has_child:
        Counter.increment()


def part2():
    data = read_input()
    init_pos = data[0].index('S')
    root = Node(init_pos, 2, None)
    populate(root, data)
    print(Counter.get_count())
    print(Counter.added_nodes)
    Counter.i = 0
    root.traverse()

    print(Counter.get_count())


if __name__ == '__main__':
    part2()
