rows, cols = [int(x) for x in input().split()]

current = 97
matrix = []
for row in range(rows):

    sub = []
    for col in range(cols):
        result = chr(current + row) + chr(current + col + row) + chr(current + row)
        sub.append(result)

    matrix.append(sub)
for x in matrix:
    print(' '.join(x))