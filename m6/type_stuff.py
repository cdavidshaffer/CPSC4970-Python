from typing import TypeVar

T = TypeVar('T')


def add(arg1: T, arg2: T) -> T:
    return arg1 + arg2


if __name__ == '__main__':
    print(add(10, 20))
    print(add(10, 15.7))

