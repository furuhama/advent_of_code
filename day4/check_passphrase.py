""" this is a code for Advent of Code 2017 Day 4 """


def shape_raw_text(file):
    f = open(file)
    data = f.read()
    f.close()

    data = data.splitlines()

    for i in range(len(data)):
        data[i] = data[i].split(' ')

    return data


def check_valid_phrase_count(word_list):
    checked = []
    for e in word_list:
        if e in checked:
            return False
        else:
            checked.append(e)

    return True


def get_char_vector(word):
    lower_cases = [chr(i) for i in range(97, 97 + 26)]
    result_vector = []
    for c in lower_cases:
        result_vector.append(word.count(c))

    return result_vector


if __name__ == '__main__':
    w = shape_raw_text('pass_phrases')

    #
    # Part 1
    #
    # count = 0
    # for e in w:
    #     if check_valid_phrase_count(e):
    #         count += 1

    # print(count)

    #
    # Part 2
    #
    ng_count = 0
    for e in w:
        checked_list = []
        for a in e:
            if get_char_vector(a) in checked_list:
                ng_count += 1
                break
            else:
                checked_list.append(get_char_vector(a))

    print(len(w) - ng_count)
