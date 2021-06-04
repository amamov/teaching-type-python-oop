from typing import List, TypeVar

T = TypeVar("T", int, str, List[int])  # T는 int, str, List[int]일 수 있습니다.


def add(a: T, b: T) -> T:
    return a + b


print(add(1, 3))  # [int, int] -> int
print(add("item", "4"))  # [str, str] -> str
print(add([1, 2], [3, 4]))  # [List[int], List[int]] -> List[int]
print(add("item", 4))  # Error!

from typing import List, TypeVar

T = TypeVar("T")


def get_first(data: List[T]) -> T:
    return data[0]


print(get_first([1, 2, 3]))  # List[int] -> int
print(get_first(["item4", "is", "developer"]))  # List[str] -> str
