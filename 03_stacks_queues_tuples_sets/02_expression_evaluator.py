from functools import reduce

string = input().split()
numbers = []

for item in string:
    if item.lstrip('-').isnumeric():
        numbers.append(int(item))
    else:
        if item == '+':
            numbers = [reduce(lambda x, y: x + y, numbers)]
        elif item == '-':
            numbers = [reduce(lambda x, y: x - y, numbers)]
        elif item == '*':
            numbers = [reduce(lambda x, y: x * y, numbers)]
        elif item == '/':
            numbers = [reduce(lambda x, y: x / y, numbers)]
print(int(numbers[0]))
