""" this is a code for Advent of Code 2017 Day 5 """


def read_num_and_get_next_target(place):
    """
    this function returns next targets place
    place and its number is in list object
    """

    return True


def check_end(place):
    """
    check if it reaches an end of input file
    """

    return True  # if it reached the end


def raw_input_file_to_list(file):
    f = open(file)
    data = f.read()
    f.close()

    data = data.splitlines()
    for i in range(len(data)):
        temp = []
        temp.append(i + 1)  # .append(int(data[i]))
        temp.append(data[i])
        data[i] = temp

    return data


if __name__ == '__main__':
    target_list = raw_input_file_to_list('my_input')  # right side works well
