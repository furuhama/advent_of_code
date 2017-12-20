""" this is a code for Advent of Code 2017 Day9 """


def get_input():
    data = input()
    return [int(i) for i in data.split(',')]


def reverse_list(input_num, c_position, input_list):
    length = len(input_list)
    result = [i for i in input_list]
    for i in range(input_num):
        to_position = get_correct_position(i + c_position + 1, length)
        from_position = get_correct_position(
            c_position + input_num - i, length)
        result[to_position] = input_list[from_position]
    return result


def get_correct_position(position, list_length):
    return position % list_length


def get_next_c_position(input_num, c_position, list_length, skip_size):
    return (c_position + input_num + skip_size) % list_length


if __name__ == '__main__':
    order_list = get_input()
    main_list = [i for i in range(256)]
    length = 256

    c_position = 0
    skip_size = 0
    for input_num in order_list:
        main_list = reverse_list(input_num, c_position, main_list)
        c_position = get_next_c_position(
            input_num, c_position, length, skip_size)
        skip_size += 1

    print(main_list)

    print("sum of first two elements is: {}".format(
        main_list[0] * main_list[1]))
