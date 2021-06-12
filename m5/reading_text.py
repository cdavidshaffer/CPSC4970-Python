if __name__ == '__main__':
    with open("green eggs and ham.txt", mode="rt", encoding="utf-8") as f:
        print(repr(f.readline()))
        print(repr(f.readline()))

    with open("fromwindows.txt", mode="rt", encoding="utf-8") as f:
        for line in f:
            print(line, end="")

    with open("kafka.txt", mode="rt", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
