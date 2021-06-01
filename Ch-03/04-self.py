# [self의 이해]
# ** self는 인스턴스 객체이다!!
# ** 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다! 즉, self는 인스턴스 그 자체이다!


class SelfTest:

    # * 클래스 변수
    name = "amamov"

    def __init__(self, x):
        self.x = x  # * 인스턴스 변수

    # * 클래스 메서드
    @classmethod
    def function1(cls):
        print(f"cls : {cls}")
        print("function 1 called !")

    # *인스턴스 메서드
    def function2(self):
        print(f"self : {self}")
        print("class안의 self의 주소:", id(self))
        print("function 2 called !")


test_instance = SelfTest(17)


print("인스턴스의 주소:", id(test_instance))
