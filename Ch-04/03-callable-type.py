# https://mypy.readthedocs.io/en/stable/kinds_of_types.html
# * Callable types
from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


print(add(1, 33))


def tets():
    pass


def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)


print(foo(tets))
