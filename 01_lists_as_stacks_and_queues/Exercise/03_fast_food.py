from collections import deque

total_food = int(input())
sequence = deque([int(x) for x in input().split()])
print(max(sequence))
while total_food and sequence:
    if total_food >= sequence[0]:
        total_food -= sequence.popleft()
    else:
        print(f'Orders left: {" ".join(str(x) for x in sequence)}')
        break
    if not sequence:
        print('Orders complete')
