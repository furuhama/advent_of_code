""" this is a code for Advent of Code 2017 Day 3 """

import math


def check_nearest_odd_sq_num(n):
    """
    in this spiral, each spiral ends with a square of odd number
    so, get which odd number spiral the target is in
    """
    i = 1
    while i ** 2 < n:
        i += 2
    # i is definitely odd number
    return i


def check_extra_steps(n, i):
    """
    in a spiral, check where the target number is
    """
    diff = i ** 2 - n
    # i is odd number
    half_len = (i - 1) // 2

    extra_steps = (diff % (i - 1)) - half_len
    return abs(extra_steps)


def check_index_value(index):
    if index == 1:
        return 1
    elif index == 2:
        return 1
    elif index == 3:
        return 2
    elif index == 4:
        return 4
    elif index == 5:
        return 5
    elif index == 6:
        return 10
    else:
        circle = (check_nearest_odd_sq_num(index) + 1) // 2
        # max_step is length of each direction steps
        max_step = (circle - 1) * 2
        extra_steps = index - ((circle - 1) * 2 - 1) ** 2
        # direction is which side the index is in (it returns 1 to 4)
        direction = math.ceil(extra_steps / max_step)
        steps = extra_steps - (direction - 1) * max_step

        def matrix_to_index(circle, direction, steps):
            if circle == 1:
                return 1
            else:
                base_index = ((circle - 1) * 2 - 1) ** 2
                max_steps = (circle - 1) * 2
                extra_index = max_steps * (direction - 1) + steps
                return base_index + extra_index

        if steps == 1:
            if direction == 1:
                return check_index_value(index - 1) + check_index_value(matrix_to_index(circle - 1, 1, 1))
            else:
                inside_index = matrix_to_index(
                    circle - 1, direction - 1, (circle - 2) * 2)
                return check_index_value(index - 1) + check_index_value(index - 2) + check_index_value(inside_index) + check_index_value(inside_index + 1)
        elif steps == max_step:
            inside_slant_index = matrix_to_index(
                circle - 1, direction, steps - 2)
            if direction != 4:
                return check_index_value(index - 1) + check_index_value(inside_slant_index)
            else:
                circle_first_index = matrix_to_index(circle, 1, 1)
                return check_index_value(index - 1) + check_index_value(inside_slant_index) + check_index_value(circle_first_index)
        elif steps == max_step - 1:
            inside_index = matrix_to_index(circle - 1, direction, steps - 1)
            if direction != 4:
                return check_index_value(index - 1) + check_index_value(inside_index) + check_index_value(inside_index - 1)
            else:
                return check_index_value(index - 1) + check_index_value(inside_index) + check_index_value(inside_index - 1) + check_index_value(inside_index + 1)
        elif steps == 2 and direction == 1:
            inside_index = matrix_to_index(circle - 1, 1, 1)
            return check_index_value(index - 1) + check_index_value(index - 2) + check_index_value(inside_index) + check_index_value(inside_index + 1)
        else:
            inside_index = matrix_to_index(circle - 1, direction, steps - 1)
            return check_index_value(index - 1) + check_index_value(inside_index - 1) + check_index_value(inside_index) + check_index_value(inside_index + 1)


if __name__ == '__main__':
    #
    # Part 1
    #

    # n = int(input())
    # i = check_nearest_odd_sq_num(n)
    # extra = check_extra_steps(n, i)
    # steps = (i - 1) // 2 + extra
    # print("{} takes {} steps".format(n, steps))

    #
    # Part 2
    #

    i = 1
    value = 0
    while value <= 361527:
        i += 1
        value = check_index_value(i)

    print("{} is value {}".format(i, value))
