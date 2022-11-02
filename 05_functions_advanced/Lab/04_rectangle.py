def rectangle(length, width):
    def area(a, b):
        result = a * b
        return result

    def perimeter(a, b):
        result = a*2 + b*2
        return result

    if isinstance(length, int) and isinstance(width, int):
        area = area(length, width)
        perimeter = perimeter(length, width)
        return f'Rectangle area: {area}\nRectangle perimeter: {perimeter}'
    else:
        return 'Enter valid values!'


print(rectangle(2, 3))