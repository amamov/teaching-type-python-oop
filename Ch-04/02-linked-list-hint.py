from typing import Optional


class Node:
    __slots__ = ("item", "pointer")

    def __init__(self, item, pointer: Optional["Node"]):
        self.item = item
        self.pointer: Optional["Node"] = pointer


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        else:
            pass


class Stack(LinkedList):
    def push(self, item):
        pass

    def pop():
        pass
