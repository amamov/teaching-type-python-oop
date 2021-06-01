# encapsulation : class 기초 사용법
# * 객체(object)의 **속성과 행위(methods)**를 하나로 묶고, 구현된 일부를 외부에 감추어 은닉한다.
# 이번 시간에는 class에 대한 기본적인 사용법을 익히는 시간을 갖도혹하겠습니다.
# 저희가 만들어볼 예제는 사칙연산 프로그램인데요.


# ** 사칙연산 계산기


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print(add(1, 2))
print(sub(1, 2))
print(mul(1, 2))
print(div(1, 2))
