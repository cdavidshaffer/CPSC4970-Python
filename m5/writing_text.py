if __name__ == '__main__':
    with open("newfile.txt", mode="wt", encoding="utf-8", newline='\r\n') as f:
        f.write("Hello world\n")
        f.write("This is a new file\n")
        f.write("Python is \U0001F44D")