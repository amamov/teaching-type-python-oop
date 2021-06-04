# https://mypy.readthedocs.io/en/stable/kinds_of_types.html
# Callable types
from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def foo2(func: Callable[[int, int], int]) -> int:
    return func(2, 3)


print(foo2(add))
