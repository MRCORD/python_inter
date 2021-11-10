def divisors(num):
    try:
        if num <= 0:
            raise ValueError("Number must be greater than 0")
        else:
            divisors = [i for i in range(1, num + 1) if num % i == 0]
    except ValueError as err:
        print(err)
    
    '''
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
    '''

def main():
    try:
        num = int(input("Enter a number: "))
        print("The divisors of", num, "are:", divisors(num))
        print('finish')
    except ValueError:
        print("That's not a number!")


if __name__ == '__main__':
    main()