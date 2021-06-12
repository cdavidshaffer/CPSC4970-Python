def f():
    try:
        return "foo"
    finally:
        return "bar"


if __name__ == '__main__':
    print(f())