# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#type-aliases

from typing import Union, List, Tuple
from typing_extensions import TypedDict

# * type alias

X = Union[int, float, bool, Union[List[str], Tuple[int]]]

xxx: X = 12


def test(x: X) -> X:
    return x


test(xxx)

# * dict alias


class Point(TypedDict):
    x: int
    y: float
    z: str


print(isinstance(True, int))

point: Point = {"x": True, "y": 8, "z": "12"}
