# https://mypy.readthedocs.io/en/stable/builtin_types.html
from typing import List, Dict

int_var: int = 9

float_var: float = 9.1

str_var: str = "hello world!"

bool_var: bool = True

# bytes는 1바이트 단위의 값을 연속적으로 저장하는 시퀀스 자료형
bytes_var: bytes = bytes(10)

none_var: None = None

# python 3.9에서는 별도의 import 없이 list_var: list[str] = ["a", "b", "c"] 라고도 작성이 가능하다.
list_var: List[str] = ["a", "b", "c"]

# python 3.9에서는 별도의 import 없이 dict[str, int]로 작성이 가능하다.
dict_var: Dict[str, int] = {"hello": 1, "world": 2}