from __future__ import annotations  # required for postponed evaluation of annotation
                                    # that is, so a class can reference itself
                                    # this will no longer be required in Python 3.10
from numbers import Real


class Vector:
    def __init__(self, x: Real, y: Real):
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other: Real) -> Vector:
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other: Real) -> Vector:
        return Vector(self.x * other, self.y * other)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


if __name__ == '__main__':
    v1: Vector = Vector(1, 2)
    v2: Vector = Vector(10, 25)
    print(v1 + v2)
    print(v1*5)
    print(5*v1)
