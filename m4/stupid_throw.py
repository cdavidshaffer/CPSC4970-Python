class DemoException(Exception):
    pass


def gen():
    try:
        yield 1
        yield 2
        yield 3
    except DemoException:
        print("Caught in gen")
    yield 99


def main():
    g = gen()
    print(next(g))
    print("Before throw")
    z = g.throw(DemoException())
    print(f"throw gave back {z}")
    print("After throw")


if __name__ == '__main__':
    main()