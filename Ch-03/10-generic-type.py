from typing import List, TypeVar

T = TypeVar("T", int, str)

ll: List[int] = [1, 2, 3, 4]

lll: List[str] = [
    "saaa",
    "asdsa",
]


def get_first(l: List[T]) -> T:
    return l[0]


print(get_first(ll))

print(get_first(lll))
