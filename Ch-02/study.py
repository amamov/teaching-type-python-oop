def function(arg1, arg2, *argsss, **ssss):
    print(arg1)
    print(arg2)
    print(args)
    print(kwargs)


function(1, 2, 3, 4, 5, name="amamov", age=12)