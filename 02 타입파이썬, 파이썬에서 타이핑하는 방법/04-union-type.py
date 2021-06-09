# https://mypy.readthedocs.io/en/stable/kinds_of_types.html

from typing import Union

xxx: Union[int, str] = 3

xxx = "17"


def foo(x: Union[int, str]) -> Union[int, str]:
    return x


foo(xxx)
