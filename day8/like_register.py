""" this is a code for Advent of Code 2017 Day7 """

#
# Part 1
#


def read_input(file):
    """
    reading input raw file and return program as a list
    this returns a list like below
    [['b', 'inc', '5', 'if', 'a', '>', '1'], ['a', 'inc', '1', 'if', 'b', '<', '5']]
    """
    f = open(file)
    data = f.read()
    f.close()

    data = [x.split(' ') for x in data.splitlines()]

    return data


if __name__ == '__main__':
    print(read_input('test_input'))
