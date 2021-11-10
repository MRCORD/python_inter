# dictionaty comprehension
# natural_numbers keys(1:101), value i**3


def main():

   # for loop
    """
    for i in range(1,101):
        if i%3 == 0:
        d[i] = i**3
    """

    # dict comprehension
    d = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    # dictionary comprehension keys(1:10001), value sqrt(i)

    r = {i: i**0.5 for i in range(1, 10001)}

    print(d)
    print(r)


if __name__ == "__main__":
    main()
