from typing import Generic, TypeVar
from collections.abc import MutableSequence

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._contents: MutableSequence[T] = []

    def push(self, value: T) -> None:
        self._contents.append(value)

    def pop(self) -> T:
        top: T = self._contents[0]
        self._contents = self._contents[1:]
        return top


if __name__ == '__main__':
    s1: Stack[int] = Stack()
    s2: Stack[str] = Stack()
    s1.push(15)
    s2.push('hello')
    print(s1.push(22))
