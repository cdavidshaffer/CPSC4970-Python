class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(10,30)
    print(p.x)           # direct access, no "getter"
    print(vars(p))
    p.x = 136            # direct access, no "setter"
    print(vars(p))
    del p.x
    print(vars(p))
