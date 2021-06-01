class Robot:

    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """

    # Class Variable 클래스 변수 (인스턴스가 공통으로 사용한다.)
    population = 0

    def __init__(self, name):  # 생성자
        self.name = name  # Instanse Variable
        Robot.population += 1

    # Instance Method
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

Robot.how_many()  # Call class method

droid2 = Robot("amamov")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
Robot.how_many()
droid2.die()
