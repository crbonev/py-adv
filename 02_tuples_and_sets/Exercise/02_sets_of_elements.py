n, m = input().split()
first = set()
second = set()
unique = set()
for _ in range(int(n)):
    first.add(int(input()))
for _ in range(int(m)):
    second.add(int(input()))

for el in first:
    if el in second:
        unique.add(el)
for el in second:
    if el in first:
        unique.add(el)
for el in unique:
    print(el)