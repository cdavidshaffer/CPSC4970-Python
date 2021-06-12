if __name__ == '__main__':
    with open('somefile.dat', mode='ab') as f:
        f.write(bytes([1, 2, 3, 4, 5, 6]))