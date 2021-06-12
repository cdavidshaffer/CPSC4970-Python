if __name__ == '__main__':
    with open("somefile.dat", mode="rb") as f:
        data = f.read()
        for b in data:
            print(hex(b))