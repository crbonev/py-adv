rows, cols = [int(x) for x in input().split()]
snake = input()
idx = 0
matrix = []
for row in range(rows):
    result = ''
    for col in range(cols):
        result += snake[idx % len(snake)]
        idx += 1
    if row % 2 == 0:
        matrix.append(result)
    else:
        matrix.append(result[::-1])

for sub in matrix:
    print(sub)



"""
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
"""