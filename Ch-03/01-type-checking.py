"""
이번 시간에는 python에서의 기본적인 타입 힌트와 타입을 체크하는 방법에 대해 알아보도록 하겠습니다.
python에서의 타입 힌트는 다음과 같이 할 수 있습니다. 먼저 공식문서를 볼까요?

int 변수에 대해서는 다음과 같이 할 수 있습니다.
str 변수에 대해서는 다음과 같이 할 수 있습니다.
bool 변수에 대해서는 다음과 같이 할 수 있습니다.

하지만 말그대로 타입 힌트이기 때문에 보시는 것처럼 타입 검사는 하지 않습니다. 
이 경우를 대비하여 일반적으로 타이핑을 하는 방법에 대해서 알아보도록 하겠습니다.

타이핑이 필요할 때를 생각해 볼까요?
예를들어 함수의 인자를 받는 경우인데요. 
특정 타입의 변수가 들어왔을 때 필요한 계산이 진행될 경우에는 타입 검사가 필요합니다.

이럴경우 isinstance라는 메서드로 검사를 하는데요 먼저 isinstance라는 메서드에 대해 알아봅시다.

주의 사항이 있습니다. bool 객체일 경우 int를 상속 받기 떄문에 bool 클래스 상속받기 떄문에 따로 예외 처리를 해야 합니다.
"""

# * type hint

xxx: int = 12
yyy: str = "hello world"
ttt: bool = True


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
    type_check(xxx, int)


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
