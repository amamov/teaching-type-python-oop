'''
staticmethod vs classmethod
'''

# [self의 이해 --> self는 인스턴스 객체이다!!
# 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다! 즉, self는 인스턴스 그 자체이다!

# 인스턴스를 통해 변수에 접근하면 파이썬은 먼저 인스턴스의 네임스페이스에서 해당 변수가 존재하는지 찾는다. 
# 해당 변수가 네임스페이스에 존재하지 않으면 클래스의 네임스페이스로 가서 다시 변수를 찾게 된다.


class SelfTest:

    ## 클래스 변수
    name = "amamov"

    ## 클래스 메서드
    @classmethod
    def function1(cls):
        print(f'cls : {cls}')
        print("function 1 called !")

    ## 인스턴스 메서드
    def function2(self):
        print("function 2 called !")
        print('class안의 self의 주소:', id(self))

    ## static method
    @staticmethod
    def function3():
        print("function 3 called !")


test_instance = SelfTest()

## 클래스 변수는 클래스의 네임스페이스에 저장된다.
print('클래스의 네임스페이스:', SelfTest.__dict__)
print('인스턴스의 네임스페이스', test_instance.__dict__)

print(SelfTest.name)
print(test_instance.name)

## 클레스 메서드는 인스턴스에서 호출 불가능
# self_instance.function1() # error

SelfTest.function1()
# function 1 called !

test_instance.function2()
# function 2 called !

SelfTest.function3()
# function 3 called !

test_instance.function3()
# function 3 called !

print('인스턴스의 주소:', id(test_instance))