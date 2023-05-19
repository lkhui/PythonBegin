from functools import wraps

def do_nothing(f):
    def inner(*args, **kwargs):
        print("damns")
        return f(*args, **kwargs)
    return inner

@do_nothing
@do_nothing
def alpha(*args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')

alpha()