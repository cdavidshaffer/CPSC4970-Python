def f():
    print('before g')
    try:
        print('before g in try')
        g()  # <-----
        print('after g in try')
    except NotImplementedError:
        print("caught in f")
    finally:
        print("finally in f")
    print('after g')


def g():
    print("before raise")
    #raise NotImplementedError("Something is wrong!")
    print("after raise")


if __name__ == '__main__':
    f()
