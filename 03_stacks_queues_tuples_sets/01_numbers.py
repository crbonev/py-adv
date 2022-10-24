first = set(int(x) for x in input().split(' '))
second = set(int(x) for x in input().split(' '))
lines = int(input())

for _ in range(lines):
    command = input().split()
    if command[0] == 'Add':
        if command[1] == 'First':
            numbers = set([int(el) for el in command if el.isdigit()])
            for num in numbers:
                first.add(num)
        elif command[1] == 'Second':
            numbers = set([int(el) for el in command if el.isdigit()])
            for num in numbers:
                second.add(num)

    elif command[0] == 'Remove':
        if command[1] == 'First':
            numbers = [int(el) for el in command if el.isdigit()]
            for num in numbers:
                if num in first:
                    first.remove(num)

        elif command[1] == 'Second':
            numbers = [int(el) for el in command if el.isdigit()]
            for num in numbers:
                if num in second:
                    second.remove(num)

    elif command[0] == 'Check':
        set_one = set(first)
        set_two = set(second)
        if set_one.issubset(set_two) or set_two.issubset(set_one):
            print('True')
        else:
            print('False')

first = sorted(first)
second = sorted(second)
print(', '.join(map(str, sorted(map(int, first)))))
print(', '.join(map(str, sorted(map(int, second)))))