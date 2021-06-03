# 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
# 인스턴스 변수 값에 대한 유효성 검사 및 수정
class Robot:

    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
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
        if new_age < 0:
            raise ValueError("age > 0")
        else:
            self.__age = new_age

    def die(self):
        if not Robot.__is_empty():
            print(f"{self.__name} is being destroyed!")
            Robot.__population -= 1
            if Robot.__population == 0:
                print(f"{self.__name} was the last one.")
            else:
                print(f"There are still {Robot.__population} robots working.")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.__name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.__population} robots."

    @staticmethod
    def are_you_robot():
        print("yes!!")

    @classmethod
    def __is_empty(cls):
        if cls.__population == 0:
            print("is empty robot")
            return True
        else:
            return False

    def __str__(self):
        return "<Robot Class >"

    def __call__(self):
        return "hello world"


droid = Robot("R2-D2", 2)


# droid.__name # error

# droid.__age = 2 # error

droid.age = 2

print(droid.age)

# droid.age = -1 # error

print(droid.name)

# droid.name = "hello"
