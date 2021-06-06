from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    __slots__ = ("item", "pointer")

    def __init__(self, item: T, pointer: Optional["Node"] = None):
        self.item = item
        self.pointer = pointer


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        cur_node = self.head
        count: int = 1
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            count += 1
        return count

    def __str__(self) -> str:
        result: str = ""
        if self.head is None:
            return result
        cur_node = self.head
        result += f"{cur_node.item}"
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            result += f", {cur_node.item}"
        return result


class Stack(Generic[T], LinkedList[T]):
    def push(self, item: T) -> None:
        new_node: Node[T] = Node[T](item=item)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node

    def pop(self) -> T:
        if self.head is None:
            raise ValueError("stack is empty")
        else:
            cur_node = self.head
        if cur_node.pointer is None:
            self.head = None
            return cur_node.item
        while cur_node.pointer.pointer is not None:
            cur_node = cur_node.pointer
        result = cur_node.pointer
        cur_node.pointer = None
        return result.item


if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(12)
    stack.push(17)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    # stack.push([123])
    # stack.push("hello world1!")

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    # stack.pop()
    stack.pop()

    print(stack.length)
    print(stack)
