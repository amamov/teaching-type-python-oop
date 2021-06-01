# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#type-aliases
from typing import Union, List, Dict
from typing_extensions import TypedDict

Hello = Union[List[str], List[int]]

x: Hello = [1, 2]


class Point(TypedDict):
    x: int
    y: float


p: Point = {"x": 1, "y": 2.2}
