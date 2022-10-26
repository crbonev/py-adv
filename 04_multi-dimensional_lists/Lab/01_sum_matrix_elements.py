rows, columns = [int(x) for x in input().split(', ')]
matrix = []
total = 0
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(rows):
    for col in range(columns):
        total += matrix[row][col]

print(total)
print(matrix)
