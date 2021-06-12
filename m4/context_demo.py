class ChattyContext:
    def __init__(self):
        print("Init context")

    def __enter__(self):
        print("Entering context")
        return 1, 2, 3

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        print("type:", exc_type, "  value:", exc_val, "  traceback: ", exc_tb)
        return False


if __name__ == '__main__':
    print("Before")
    with ChattyContext() as (a, b, c):
        print(f"Inside   a: {a}   b: {b}   c: {c}")
        x = 1 / 0
        print("Still inside")
    print("After")
