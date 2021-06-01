# _ : __는 안 이쁘므로 일반적으로는 _으로 하고 암묵적으로 약속한다.
# __ : private
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

droid.say_hi()

# droid.__name # error


print(droid.how_many())

droid.die()

droid.die()