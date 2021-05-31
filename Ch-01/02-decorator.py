# 데코레이터


def decorator(func):
    def inner():
        print("This is emoticon")
        func()

    return inner


def smile():
    print("^_^")


smile = decorator(smile)
smile()


@decorator
def confused():
    print("@_@")


confused()

import time

# 함수의 퍼포먼스를 체크하는 데코레이터 개발


def performance_clock(func):
    def performance_clocked(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        print(f"{start_time} -> {end_time} : {round(end_time - start_time, 8)}")
        return result

    return performance_clocked


@performance_clock
def time_checker(second):
    time.sleep(second)


@performance_clock
def test(numbers):
    total = 0
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total += i + j + k
    return total


# time_checker(3)
test(range(30))
test(range(100))
