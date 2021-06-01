import sys
from pathlib import Path

# 상위 디렉토리를 import하기 위해 sys.path에 상위 디렉토리 경로를 추가해준다.
BASE_DIR = str(Path(__file__).resolve().parent.parent)  # 기준이되는 경로
sys.path.append(BASE_DIR)  # sys.path에 기준이되는 경로를 추가한다.

from s_module import S2  # sys.path[0]의 경로(현재 패키지)에서 찾았다.
from f_module import F  # sys,path[-1]의 경로(추가해준 경로)에서 찾았다.
from pkg1.s_module import S1  # sys,path[-1]의 경로(추가해준 경로)에서 찾았다.

if __name__ == "__main__":
    print(sys.path)
    print(F())
    print(S1())
    print(S2())