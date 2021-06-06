# class types


class Hello:
    def world(self) -> int:
        return 7


class World:
    pass


hello: Hello = Hello()
world: World = World()


def foo(ins: Hello) -> int:
    return ins.world()


print(foo(hello))


# * class type 보충

from typing import Optional


class Node:
    def __init__(self, data: int, node: Optional["Node"] = None):
        self.data = data
        self.node = node


node2 = Node(12)

node1 = Node(27, node2)

node0 = Node(30, node1)
