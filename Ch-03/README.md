# typing

1. 가상환경에 들어간다.

2. `pip install mypy`

3. `mypy main.py`

## 주의사항

- python은 애초에 타이핑이 없는 언어이고 mypy라는 패키지의 도움을 받는 것이므로 타이핑에 너무 집착하지 말자
- 특정 단위의 알고리즘을 개발할 때 국소적으로 mypy를 사용하여 예상치 못한 에러를 잡아내자. mypy에 깊게 의존하지 말자.
- 타입힌트는 적극적으로 사용하자. 실제로 현재 공식문서에서 적극적으로 지원되고 있다.
- 협업 시에 매우 유용하고 변수 네이밍에도 효율적이다.

```python
def train():
    input_data = Asjdkl
    data: str = "123"

    # asdjljkasd
```