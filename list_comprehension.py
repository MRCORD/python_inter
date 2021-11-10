def run():

    # for loop
    """ 
    squares = []
        for i in range(1,101):
            if i % 3 !=0:
                squares.append(i**2)
    """

# list comprehension

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    lista = [i for i in range(1, 100000) if (
        i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]

    print(f' squares: {squares}')
    print(f'reto: {lista}')


if __name__ == '__main__':
    run()
