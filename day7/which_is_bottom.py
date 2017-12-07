""" this is a code for Advent of Code 2017 Day7 """

#
# Part 1
#

"""
every node, except root node, has their parent node
so, check every node whether it has parent or not
"""


def raw_input_to_list(file):
    """
    format of each line is
    'hoge (num) -> fuga, piyo'
    """
    f = open(file)
    data = f.read()
    f.close()

    data = data.splitlines()

    node_lists = []

    for i in data:
        one_line = []
        temp = i.split(' (')
        one_line.append(temp[0])

        if '->' in temp[1]:
            # the line below returns list like ['hoge', 'fuga', 'piyo']
            temp = temp[1].split(' -> ')[1].split(', ')

            for e in temp:
                one_line.append(e)

        node_lists.append(one_line)

    return node_lists


if __name__ == '__main__':
    print(raw_input_to_list('input'))
