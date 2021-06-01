class Robot:

    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

    @staticmethod
    def are_you_robot():
        print("yes!!")


droid1 = Robot("R2-D2")
droid1.say_hi()

Robot.how_many()

droid2 = Robot("amamov")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
Robot.how_many()
droid2.die()

# //* dir() : 모든 속성 값을 알 수 있다.
# //* __dict__ : 네임스페이스를 확인할 수 있다.
# //* __doc__ : class의 주석을 확인한다.
# //* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
