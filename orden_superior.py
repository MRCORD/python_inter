
def main():

    # filter
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    # odd_list = [i for i in my_list if i % 2 != 0]

    odd_list = list(filter(lambda x: x % 2 != 0, my_list))

    # map
    my_list2 = [1, 2, 3, 4, 5]
    square_list = list(map(lambda x: x ** 2, my_list2))

    # reduce
    my_list3 = [2, 2, 2, 2, 2]

    from functools import reduce

    all_multiplied = reduce(lambda x, y: x * y, my_list3)

    '''
    all_multiplied = 1
    
    for i in my_list3:
        all_multiplied *= i
    '''

    print(odd_list)
    print(square_list)
    print(all_multiplied)


if __name__ == '__main__':
    main()
