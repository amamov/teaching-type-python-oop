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

# * generic 2

K = TypeVar("K", int, list)
L = TypeVar("L")


class Robot(Generic[K, L]):
    def __init__(self, arm: K, head: L):
        self.arm = arm
        self.head = head


robot = Robot[int, str](12, "hello")

print(robot.arm)
print(robot.head)

# * generic 3


class Siri(Generic[K, L], Robot[K, L]):
    pass


siri = Siri[int, int](28, 99)

print(siri.arm)
