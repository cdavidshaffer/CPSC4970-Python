class InvalidArgument(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value


def sqrt(x):
    """
    Compute the square root of x using the Babylonian method.  Currently uses a relative tolerance of 1.e-6
    Args:
        x: a non-negative number

    Returns: the square root of x if x is non-negative
    Throws: InvalidArgument if x is negative

    """
    if x < 0:
        raise InvalidArgument("sqrt argument must be non-negative", x)
    if x == 0:
        return 0
    previous = x / 2
    next_value = 0.5*(previous + x/previous)
    while abs(next_value - previous) / previous > 1.0e-6:
        previous = next_value
        next_value = 0.5*(previous + x/previous)
    return next_value


def some_other_thing(y):
    # do some calculations...
    try:
        x = sqrt(y - 2)
    except InvalidArgument as ex:
        if ex.value == -1:
            raise InvalidArgument("can't deal with it", ex.value) from ex
    # do some more calculations...
    answer = 5*x + 2
    return answer


def something():
    value = 1
    print(some_other_thing(float(value)))


if __name__ == '__main__':
    something()
