"""
* 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술
"""

from typing import Union, Optional, TypeVar, Generic

T = TypeVar("T", int, float, str)
K = TypeVar("K", int, float, str)


class Robot(Generic[T, K]):
    def __init__(self, arm: T, head: K):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호를 해독하는 코드
        # 복잡
        pass


robot1 = Robot[int, int](12231413, 23908409)
robot2 = Robot[str, int]("12890309123", 79878789)
robot3 = Robot[float, str](1239.01823, "3243245")


class Siri(Generic[T, K], Robot[T, K]):
    pass


siri1 = Siri[int, int](12231413, 23908409)
siri2 = Siri[str, int]("12890309123", 79878789)
siri3 = Siri[float, str](1239.01823, "3243245")

print(siri1.arm)

# * function


def test(x: T) -> T:
    print(x)
    print(type(x))
    return x


test(898)
