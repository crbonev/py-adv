lines = int(input())
periodic_table = set()
for _ in range(lines):
    periodic_table.update(input().split())

for element in periodic_table:
    print(element)