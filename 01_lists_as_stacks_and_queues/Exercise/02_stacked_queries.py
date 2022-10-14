lines = int(input())
stack = []
while lines:
    query = input().split()
    if query[0] == '1':
        num = query[1]
        stack.append(int(num))
    elif query[0] == '2' and stack:
        stack.pop()
    elif query[0] == '3' and stack:
        print(max(stack))
    elif query[0] == '4' and stack:
        print(min(stack))
    lines -= 1


print(', '.join(str(x) for x in stack[::-1]))
