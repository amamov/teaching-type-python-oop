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


print(foo(world))
