from typing import List, Tuple, Dict

int_var: int = 88
str_var: str = "hello world"
float_var: float = 88.9
bool_var: bool = True

list_var: List[str] = ["1", "2", "3"]
tuple_var: Tuple[int, ...] = (1, 3, 4)

dic_var: Dict[str, int] = {"hello": 47}


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


def cal_add(x: int, y: int) -> int:
    # code
    # type_check(x, int)
    # type_check(y, int)
    return x + y


print(cal_add(1, 3))

# print(cal_add("1, ", "3, dsjkakljas"))

# print(cal_add([1, 3], [4, 5]))

# * isinstance(obj, class)

# print(isinstance("ashdjkasd", str))
# print(isinstance(88.9, float))

print(int_var)
