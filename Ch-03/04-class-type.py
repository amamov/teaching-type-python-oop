# class types


class Hello:
    def world(self) -> int:
        return 7


class World:
    pass


hello: Hello = Hello()
world: World = World()


def foo(ins: Hello) -> int:
    return ins.world()


print(foo(hello))


# * class type 보충


class Wow:
    def __init__(self, data: "Hello"):
        self.data = data


wow = Wow(hello)

print(wow.data)
