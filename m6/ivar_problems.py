class A:
    def __init__(self):
        super().__init__()
        self.__x = 0

    def change_x(self):
        self.__x += 2

    def print(self):
        print(f"{self.__x} is even")


class B:
    def __init__(self):
        super().__init__()
        self.__x = 0

    def make_a_change(self):
        self.__x = 1


class C(A, B):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    c = C()
    c.make_a_change()
    c.print()

