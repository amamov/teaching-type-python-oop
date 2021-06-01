# decorator


def copyright(username):
    def inner(func):
        def new_func(*args, **kwargs):
            print(f"@ {username}")
            func(*args, **kwargs)

        return new_func

    return inner


@copyright("yss")
def yss_emoticon(name):
    print(name)


@copyright("yrr")
def yrr_emoticon(name):
    print(name)


yss_emoticon("🙃")
yss_emoticon("🤯")
yss_emoticon("🥰")

yrr_emoticon("🙃")
yrr_emoticon("🤯")
yrr_emoticon("🤯")