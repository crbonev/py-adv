rows = int(input())
matrix = [input().split(', ') for _ in range(rows)]
primary, secondary = [], []

for idx in range(rows):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][len(matrix[idx]) - idx - 1])
print(f'Primary diagonal: {", ".join([str(x) for x in primary])}. Sum: {sum(int(x) for x in primary)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary])}. Sum: {sum(int(x) for x in secondary)}')
