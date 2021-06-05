# https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class

from __future__ import annotations
from typing import TypeVar, Optional

T = TypeVar("T")


class Node:
    __slots__ = ("item", "pointer")

    def __init__(self, item: T, pointer: Optional[Node]):
        self.item = item
        self.pointer = pointer


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
