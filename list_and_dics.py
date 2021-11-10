def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dic = {'firstname': 'John', 'lastname': 'garcia'}

    super_list = [
        {'firstname': 'John', 'lastname': 'garcia'},
        {'firstname': 'susana', 'lastname': 'torres'},
        {'firstname': 'pedro', 'lastname': 'rodelo'},
        {'firstname': 'miguel', 'lastname': 'matinez'},
        {'firstname': 'facundo', 'lastname': 'garcia'}
    ]

    super_dic = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.2, 3.3, 4.4, 5.5],
    }

    for key, value in super_dic.items():
        print(f"{key} : {value}")

    for i in super_list:
        print(f"{i['firstname']} {i['lastname']}")


if __name__ == '__main__':
    run()
