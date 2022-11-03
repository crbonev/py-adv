def even_odd(*args):

    numbers = args[:-1]
    command = args[-1]

    if command == 'even':
        even = [x for x in numbers if x % 2 == 0]
        return even
    elif command == 'odd':
        odd = [x for x in numbers if x % 2 != 0]
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))