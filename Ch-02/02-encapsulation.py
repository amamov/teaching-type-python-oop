class Robot:

    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """

    # Class Variable 클래스 변수 ()
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

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

    # 매직 메서드
    def __str__(self):
        # str 함수가 호출되었을 때 호출된다. (객체를 문자열화 하는데에 초점이 맞춰져 있다.)
        return "<Robot Class >"

    def __call__(self):
        # 인스턴스가 호출가능하도록 해준다. (callable)
        return "hello world"


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

# //* dir() : 모든 속성 값을 알 수 있다.
# //* __dict__ : 네임스페이스를 확인할 수 있다.
# //* __doc__ : class의 주석을 확인한다.
# //* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
