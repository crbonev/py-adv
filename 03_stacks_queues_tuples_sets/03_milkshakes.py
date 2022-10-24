from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque(int(x) for x in input().split(', '))
milkshakes = 0

while milkshakes < 5 and chocolate and milk:
    flag = False
    if chocolate[-1] <= 0:
        chocolate.pop()
        flag = True
    if milk[0] <= 0:
        milk.popleft()
        flag = True
    if flag:
        continue
    if chocolate[-1] == milk[0]:
        milkshakes += 1
        chocolate.pop()
        milk.popleft()
    else:
        milk.append(milk.popleft())
        chocolate[-1] -= 5

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f"Chocolate: empty" if not chocolate else f"Chocolate: {', '.join(str(x) for x in chocolate)}")
print(f"Milk: empty" if not milk else f"Milk: {', '.join(str(x) for x in milk)}")
