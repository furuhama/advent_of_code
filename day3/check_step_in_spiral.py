""" this is a code for Advent of Code 2017 Day 3 """


def check_nearest_odd_sq_num(n):
    i = 1
    while i ** 2 < n:
        i += 2
    # i is definitely odd number
    return i


def check_extra_steps(n, i):
    diff = i ** 2 - n
    # i is odd number
    half_len = (i - 1) // 2

    extra_steps = (diff % (i - 1)) - half_len
    return abs(extra_steps)


if __name__ == '__main__':
    n = int(input())
    i = check_nearest_odd_sq_num(n)
    extra = check_extra_steps(n, i)

    steps = (i - 1) // 2 + extra

    print("{} takes {} steps".format(n, steps))
