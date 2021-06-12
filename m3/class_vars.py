class ClassVarDemo:
    a_class_variable = 99


if __name__ == '__main__':
    c = ClassVarDemo()
    print(dir(c))