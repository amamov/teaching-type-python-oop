# decorator


def function(arg1, arg2, *args, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwargs)


function(1, 2, 3, 4, 5, 6, username="amamov", password="1205")


def copyright(func):
    def new_func(*args, **kwargs):
        print("@ amamovsdfjkldjsakfljdskaljfkdsla")
        func(*args, **kwargs)

    return new_func


@copyright
def emoticon(name):
    print(name)


emoticon("🙃")
emoticon("😘")
emoticon("🤯")
