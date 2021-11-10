
def palindrome(word):
    try:
        if len(word) == 0:
            raise ValueError("Word is empty")
        return word == word[::-1]
    except ValueError as e:
        print(e)
        return False


try:
    print(palindrome(""))
except TypeError:
    print("Please enter a string")