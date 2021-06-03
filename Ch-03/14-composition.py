"""
#* composition
#* 다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않을 경우
#* 1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 한다.
#* 2. 부모 클래스의 메서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가
"""


class Robot:

    """
    Robot Class
    """

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    @property
    def name(self):
        return f"yoon {self.__name}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age - self.__age == 1:
            self.__age = new_age
        else:
            raise ValueError()

    def __say_hi(self):
        self.cal_add(1, 3)
        print(f"Greetings, my masters call me {self.__name}.")

    def cal_add(self, a, b):
        return a + b + 1

    @classmethod
    def how_many(cls):
        return f"We have {cls.__population} robots."


class Siri(Robot):
    def say_apple(self):
        print("hello my apple")


class SiriKo(Robot):
    def say_apple(self):
        print("안녕 사과")


class Bixby(Robot):
    def say_sanmgsung(self):
        print("hello my sangsung")


class BixbyKo(Robot):
    def say_samsung(self):
        print("안녕 삼성")


class BixbyCal:
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)
