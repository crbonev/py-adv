def fill_the_box(a, b, c, *args):
    space = a * b * c
    cubes = args
    result = 0
    for x in cubes:
        if x != 'Finish':
            result += x
        else:
            break
    total = space - result
    if total > 0:
        return f'There is free space in the box. You could put {total} more cubes.'
    else:
        return f'No more free space! You have {abs(total)} more cubes.'


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))