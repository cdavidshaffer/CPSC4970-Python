import functools


def log(func):
    @functools.wraps(func)
    def log_and_call(*pargs, **kwargs):
        print(f"-- Calling {func.__name__}")
        print(f"-- \tpargs: {pargs}")
        print(f"-- \tkwargs: {kwargs}")
        return func(*pargs, **kwargs)
    return log_and_call


@log
def count():
    """I count from 1 to 3"""
    for i in range(3):
        print(i)


@log
def another(x, y, z=None):
    print("another function")


class CallCounter:
    def __init__(self, func):
        self.count = 0
        self._func = func

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self._func(*args, **kwargs)


@CallCounter
def g():
    print("g called")


if __name__ == '__main__':
    g()
    print(g.count)
    g()
    g()
    g()
    print(g.count)

# Output
# g called
# 1
# g called
# g called
# g called
# 4
