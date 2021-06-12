def sum_file_lines(name):
    """
    name will be a file name for an existing file containing a collection of integer strings, one per line.
    Return the sum of those integers.

    Args:
        name: file name

    Returns: the sum of the integer lines in this file

    """
    with open(name, "r") as f:
        return sum([int(line) for line in f.readlines()])


if __name__ == '__main__':
    print(sum_file_lines("numbers.txt"))
