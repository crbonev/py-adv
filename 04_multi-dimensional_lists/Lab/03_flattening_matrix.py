rows = int(input())
matrix = []
flat = []
for _ in range(rows):
    matrix.append([x for x in input().split(', ')])
flat = [int(num) for sublist in matrix for num in sublist]

print(flat)
