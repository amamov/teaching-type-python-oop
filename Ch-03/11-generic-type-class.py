from typing import TypeVar, Generic, List


T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self.data: List[T] = []

    def push(self, item) -> None:
        self.data.append(item)

    def pop(self) -> T:
        return self.data.pop()

    def __str__(self) -> str:
        return f"{self.data}"


stack = Stack[int]()

stack.push(12)
stack.push(13)
print(stack)
