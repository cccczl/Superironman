# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError(f'invalid value: {s}')
    return 10 / n

foo('0')

