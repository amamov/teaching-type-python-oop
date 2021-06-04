# class types
class Hello:
    def world(self) -> int:
        return 2


def foo(hello: Hello) -> None:
    print(hello.world())


hello: Hello = Hello()


foo(hello)