# ** packing


def function(arg1, arg2, *args, **kwargs):
    print("arg1 : ", arg1)
    print("arg2 : ", arg2)

    print("args : ", args)
    print("args type : ", type(args))

    print("kwargs : ", kwargs)
    print("kwargs : ", type(kwargs))
    return arg1 + arg2


function(1, 2, 3, 4, 5, 6, 7, 8, 9, what=False, why=True, Hello="Hello world!")

# ** unpacking


t = [1, 2, 3]

print(t)
print(*t)
print(1, 2, 3)


def func(*arg):
    print(arg)


func(1, 2, 3)

dic = {"a": 12, "b": 14, "c": 13}

dic2 = {"d": 15, **dic}

print(dic2)


# ** lambda


def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10

print(var_func)
# <function mul_10 at 0x7fed96ec15f0> : 함수의 객체가 생성되어 메모리에 할당되었다.
print(id(var_func))
# 4483604336
print(type(var_func))
# <class 'function'>

# 익명 함수로 메모리를 절약하고 가독성을 향상시킨다.
lambda_mul_10 = lambda num: num * 10

print(lambda_mul_10)
# <function <lambda> at 0x7f876258e3b0>

print(lambda_mul_10(10))
# 100