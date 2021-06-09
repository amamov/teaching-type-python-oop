# * Optional type

from typing import Union, Optional


def foo(name: str) -> Optional[str]:
    if name == "amamov":
        return None
    else:
        return name


xxx: Optional[str] = foo("amamov")
