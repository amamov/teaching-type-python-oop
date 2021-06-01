# decorator 실습

# ** 함수 성능 계산하는 데코레이터 개발


import time


def performance_checker(func):
    def new_func(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"performance : {round(end_time - start_time, 8)}")
        return result

    return new_func


# ** [decorator 실습]

# ** 함수 성능 계산하는 데코레이터 개발


@performance_checker
def test_func(ranger):
    total = 0
    for i in ranger:
        for j in ranger:
            for k in ranger:
                total = total + i + j + k
    return total


test_func(range(10))
test_func(range(100))