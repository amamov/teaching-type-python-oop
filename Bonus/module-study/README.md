## 모듈 (module)

- 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다.
- 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있다.

## 패키지 (package)

- 패키지는 모듈을 디렉토리 형식으로 구조화한 것이다.
- 모듈들은 넣어둔 디렉토리명이 패키지명이 된다.
- 패키지에는 `__init__.py` 가 반드시 존재해야 한다. (3.3버전 이후로는 `__init__.py`가 없어도 패키지로 인식한다.)
- `__init__.py`은 패키지 생성자로서 패키지 안의 모듈을 실행할때 가장 처음으로 실행된다.

## 파이썬이 모듈과 패키지를 검색하는 순서

1.`sys.moudules`

- Python이 module이나 package를 찾기 위해 우선적으로 살피는 영역으로 dictionary형태로 되어 있다. python을 실행하고 한 번 이상 import가 되었다면 다시 모듈을 찾지 않고 곧바로 sys.modules를 확인하여 module이나 package를 사용하게 된다.

2. built-in modules

   - 파이썬에서 공식으로 제공하는 라이브러리.

3. `sys.path`

   - path를 따라 모듈과 패키지를 검색한다.
   - 리스트 구조(string 요소)이고 첫 번째 리스트 요소부터 마지막까지 순회하며 모듈 또는 패키지를 찾는다.
   - sys.path에서도 모듈을 발견하지 못하면 ModuleNotFoundError 에러를 리턴한다.

## 상대경로 import

- `"from . import f_module"` : 현재 디렉토리(패키지)의 f_module을 import한다.

- `"from ... import f_module"` : 상위 디렉토리(패키지)의 f_module을 import한다.

- `"python -m pkg.main.py"` 형식으로 실행해햐 한다.

- python 공식 문서에는 상대경로보다 `sys.path`에 경로를 추가하여 import 하는 것을 권장한다.
