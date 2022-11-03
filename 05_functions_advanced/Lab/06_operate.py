def operate(operator, *args):

    def add(*args):
        return sum(args)

    def subtract(x, *args):
        result = x
        for i in args:
            result -= i
        return result

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    def divide(x, *args):
        result = x
        for x in args:
            result /= x
        return result

    if operator == '+':
        return add(*args)
    elif operator == '-':
        return subtract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return divide(*args)


print(operate("/", 2, 2, 3))
