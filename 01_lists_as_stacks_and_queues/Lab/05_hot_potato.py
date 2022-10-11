from collections import deque

kids = deque(input().split(' '))
tosses = int(input())

current = 0
while len(kids) > 1:
    current += 1
    kid = kids.popleft()
    if current < tosses:
        kids.append(kid)
    else:
        print(f'Removed {kid}')
        current = 0
else:
    kid = kids.pop()
    print(f'Last is {kid}')
