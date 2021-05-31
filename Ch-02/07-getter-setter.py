'''
getter vs setter
'''

class Test():
    def __init__(self):
        self.user = "amamov"

    @property
    def age(self):
        
        return 17
    
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            return "fuck"
        else:
            return new_age


test = Test()

# 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
# 인스턴스 변수 값에 대한 유효성 검사 및 수정