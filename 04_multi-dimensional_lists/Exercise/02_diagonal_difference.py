rows = int(input())
matrix = [input().split() for _ in range(rows)]
primary, secondary = [], []
abs1 = 0
abs2 = 0

for idx in range(rows):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][len(matrix[idx]) - idx - 1])
for num in primary:
    abs1 += int(num)
for num in secondary:
    abs2 += int(num)

print(abs(abs2 - abs1))
