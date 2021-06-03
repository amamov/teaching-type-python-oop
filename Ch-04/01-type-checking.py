class Typer:
    def str_type_check(self, x):
        if isinstance(x, str):
            pass
        else:
            raise TypeError("Type Error : str")

    def int_type_check(self, x):
        if isinstance(x, int):
            pass
        else:
            raise TypeError("Type Error : int")


typer = Typer()

xxx: str = "12312"
typer.int_type_check(xxx)
