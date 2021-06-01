import sys
from f_module import F
from pkg1.s_module import S1
from pkg2.s_module import S2

if __name__ == "__main__":
    print(sys.path)
    print(F())
    print(S1())
    print(S2())