class Test:
    pass


test = Test()

isinstance(test, Test)
isinstance(12, int)
isinstance("sss", str)


def type_check(obj, typer):
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"type error : {typer}")


def foo(value):
    type_check(value, int)
    # code ...


xxx = 12
type_check(xxx, int)

yyy = "123123"
type_check(yyy, str)

ttt = True
# * 주의 !
# type_check(ttt, int)
# print(isinstance(True, int))
# print(isinstance(True, bool))
type_check(ttt, bool)
# type_check(xxx)


# * type hint

xxx: int = 12
yyy: str = "hello world"
ttt: bool = True
