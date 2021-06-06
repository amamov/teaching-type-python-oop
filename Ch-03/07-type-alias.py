# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#type-aliases

from typing import Union, List, Tuple, Dict, Optional
from typing_extensions import TypedDict

# * type alias

Value = Union[
    int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]
]

X = int

x: X = 8

value: Value = 17


def cal(v: Value) -> Value:
    # ddmasda
    return v


# * dict alias


ddd: Dict[str, Union[str, int]] = {"hello": "world", "world": "wow!!", "hee": 17}


class Point(TypedDict):
    x: int
    y: float
    z: str
    hello: int


point: Point = {"x": 8, "y": 8.4, "z": "hello", "hello": 12}
