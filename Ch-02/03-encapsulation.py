'''
Object Oriented Programming
OOP란 프로그래밍에서 필요한 데이터를 추상화시켜 상태와 행위를 가진 객체를 만들고 그 객체들 간의 유기적인 상호작용을 통해 로직을 구성하는 프로그래밍 방법이다.

프로그램을 실제 세상에 가깝게 모델링하는 기법

> **class(클래스)란 어떤 문제를 해결하기 위한 데이터를 만들기 위해 OOP 원칙에 따라 집단에 속하는 속성(attribute)과 행위(behavior)를 변수와 메서드로 정의한 것을 의미한다.**

> **instance(인스턴스)란 클래스에서 정의한 것을 토대로 실제 메모리상에 할당된 것으로 실제 프로그램에서 사용되는 데이터이다.**

OOP 원칙 캡슐화, 추상화, 상속, 다양화
캡슐화와 상속을 위주로 추상화와 다양화는 django를 하면서 익히게 될 것

캡슐화는 객체의 속성(data fields)과 행위(methods)를 하나로 묶고, 실제 구현 내용 일부를 외부에 감추어 은닉한다.

추상화는 불필요한 정보는 숨기고 중요한 정보만을 표현함으로써 공통의 속성이나 기능을 묶어 이름을 붙이는 것이다.

상속은 부모클래스의 속성과 기능을 그대로 이어받아 사용할 수 있게하고 기능의 일부분을 변경해야 할 경우 상속받은 자식클래스에서 해당 기능만 다시 수정(정의)하여 사용할 수 있게 하는 것이다.

다양성이란 하나의 변수명, 함수명 등이 상황에 따라 다른 의미로 해석될 수 있는 것이다.
'''

class Robot:

    """
    Robot Class
    Date : ??:??:??
    """

    # Class Variable
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


