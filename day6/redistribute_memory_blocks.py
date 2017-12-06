""" this is a code for Advent of Code 2017 Day 6 """


def shape_raw_input_to_int_list(file):
    f = open(file)
    data = f.read()
    f.close()

    data = data.split()

    for i in range(len(data)):
        data[i] = int(data[i])

    return data


def which_is_max(memory):
    """
    get list & return the place of maximum number
    """
    maximum = max(memory)
    num_list = []
    for i in range(len(memory)):
        if memory[i] == maximum:
            num_list.append(i)

    return num_list


def redistribute_blocks(block_list):
    """
    main function
    """
    memory_size = len(block_list)
    maximum_place = which_is_max(block_list)[0]
    maximum_block = block_list[maximum_place]

    base_distribution = maximum_block // memory_size
    extra_blocks = maximum_block % memory_size

    # redistribution start
    # redistribute base blocks
    block_list[maximum_place] = 0
    for i in range(len(block_list)):
        block_list[i] += base_distribution

    # redistribute extra blocks
    for j in range(extra_blocks):
        target_place = maximum_place + 1 + j
        if target_place >= memory_size:
            target_place -= memory_size
        block_list[target_place] += 1

    return block_list


def check_and_update_stock(stock_memory, block_list, f):
    if block_list in stock_memory:
        f = True
        return stock_memory
    else:
        stock_memory.append(block_list)
        f = True
        return stock_memory


if __name__ == '__main__':
    #
    # Part 1
    #

    # blocks = shape_raw_input_to_int_list('my_input')

    #
    # Part 2
    #

    blocks = [1, 1, 14, 13, 12, 11, 10, 9, 8, 7, 7, 5, 5, 3, 3, 0]
    flag = False
    stock = []
    counts = 0

    while not flag:
        blocks = redistribute_blocks(blocks)
        if (blocks in stock):
            flag = True
        else:
            stock.append([])
            for i in range(len(blocks)):
                stock[counts].append(blocks[i])

        counts += 1

    print(counts)
