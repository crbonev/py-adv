from collections import deque
#
# numbers = deque(map(int, input().split()))
# target = int(input())
# couples = []
# count = 0
# lst = []
#
# while numbers:
#     first = numbers.popleft()
#     for num in numbers:
#         if first + num == target:
#             print(f'{first} + {num} = {target}')
#             couples.append((first, num))
#         count += 1
#
# print(f'Iterations done: {count}')
#
# for element in couples:
#     if element not in lst:
#         lst.append(element)
# print('\n'.join(str(x) for x in lst))

numbers = list(map(int, input().split()))
target = int(input())
pairs = set()
iterations = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        first = numbers[i]
        second = numbers[j]
        if first + second == target:
            pairs.add((first, second))
            print(f'{first} + {second} = {target}')
        iterations +=1

print(f'Iterations done: {iterations}')

for pair in pairs:
    print(pair)
