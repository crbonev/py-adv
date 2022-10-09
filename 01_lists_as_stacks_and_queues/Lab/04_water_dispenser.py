from collections import deque

water = int(input())
que = deque()

while True:
    people = input()
    if people != 'Start':
        que.append(people)
    else:
        break

while True:
    command = input().split()
    if len(command) == 1:
        if command[0] == 'End':
            print(f'{water} liters left')
            break
        liters = int(command[0])
        if liters <= water:
            water -= liters
            person_name = que.popleft()
            print(f'{person_name} got water')
        else:
            liters = int(command[0])
            person_name = que.popleft()
            print(f"{person_name} must wait")
    else:
        liters = int(command[1])
        water += liters

