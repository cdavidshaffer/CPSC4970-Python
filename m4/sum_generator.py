class ResetSum(Exception):
    def __zap__(self):
        pass


def sum_generator():
    current_sum = 0
    while True:
        try:
            n = yield current_sum
            current_sum += n
        except ResetSum:
            current_sum = 0


if __name__ == '__main__':
    g = sum_generator()
    print(g.send(None))
    print(g.send(1))
    print(g.send(1))
    print(g.send(1))
    print("reset: ", g.throw(ResetSum()))
    print(g.send(1))
    print(g.send(1))
    g.close()
    print(g.send(1))
