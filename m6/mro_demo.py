class Top:
    def __init__(self):
        self._x = 0


class A:
    def __init__(self):
        self._y = 42


class B(A, Top):
    def __init__(self):
        super().__init__()
        super(A, self).__init__()


if __name__ == '__main__':
    b = B()
    x = 2
