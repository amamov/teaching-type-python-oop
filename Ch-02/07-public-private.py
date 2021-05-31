# _ : __는 안 이쁘므로 일반적으로는 _으로 하고 암묵적으로 약속한다.
# __ : private

class Test():

    def __init__(self):
        self.__username = "amamov"


class T2(Test):

    pass



test = Test()


print(dir(test))
