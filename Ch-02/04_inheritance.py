
'''
클래스 상속
메서드 오버라이딩
Python의 모든 클래스는 object 클레스를 직접 혹은 간접 상속한다.
Super 클래스를 Sub 클래스가 상속받았을 때 Super 클래스를 부모 클래스(슈퍼 클래스)라고 하고 Sub 클래스를 자식 클래스(서브 클래스)라고 정의한다.

부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에도 담긴다.

자식 클래스에는 별도의 메서드를 추가할 수 있다.

관련 함수 : MyClass.mro() --> 상속 관계를 보여준다.
'''

class Robot:

    """
    Robot Class
    """

    population = 0

    def __init__(self, name): 
        self.name = name  
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

# ** 상속

class Amaco(Robot):
    pass


# ** 오버라이딩

class Amaco(Robot):

    def say_hi(self):
        pass

# **super

class Amaco(Robot):

    def __init__(self):
        super().__init__(value)

    def say_hi(self):
        super().say_hi()

# ** python의 비밀
# 파이썬의 모든 것들은 object에 상속받는다.

class A(object):
    pass

# ** 다중상속

class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]