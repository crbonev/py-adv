from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())
total_honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        symbol = symbols.popleft()
        collected, bee = nectar.pop(), bees.popleft()
        if symbol == '+':
            total_honey += abs(bee + collected)

        elif symbol == '-':
            total_honey += abs(bee - collected)

        elif symbol == '*':
            total_honey += abs(bee * collected)

        elif symbol == '/':
            if nectar == 0 or bee == 0:
                continue
            total_honey += abs(bee / collected)

    else:
        nectar.pop()

print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')