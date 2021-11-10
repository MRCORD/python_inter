def divisors(num):

    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def main():

    num = input("Enter a number: ")
    assert num.isnumeric(), "Please enter a number"
    print("The divisors of", num, "are:", divisors(num))
    print('finish')


if __name__ == '__main__':
    main()
