""" this is a code for Advent of Code 2017 Day 5 """


def read_num_and_get_next_target(arg_map, place):
    """
    this function returns next targets place
    place and its number is in list object
    """
    number = arg_map[place][1]
    next_place = place + number

    #
    # part 1
    #

    # increase the number after move
    # arg_map[place][1] += 1

    #
    # part 2
    #

    if arg_map[place][1] >= 3:
        arg_map[place][1] -= 1
    else:
        arg_map[place][1] += 1
    return next_place


def check_end(arg_map, place):
    """
    check if it reaches an end of input file
    """
    if place + 1 > len(arg_map):
        return True
    else:
        return False


def raw_input_file_to_list(file):
    f = open(file)
    data = f.read()
    f.close()

    data = data.splitlines()
    for i in range(len(data)):
        temp = []
        temp.append(i + 1)  # .append(int(data[i]))
        temp.append(int(data[i]))
        data[i] = temp

    return data


if __name__ == '__main__':
    n = input()
    target_map = raw_input_file_to_list(n)

    place = 0
    count = 0
    while not check_end(target_map, place):
        count += 1
        place = read_num_and_get_next_target(target_map, place)

    print(count)
