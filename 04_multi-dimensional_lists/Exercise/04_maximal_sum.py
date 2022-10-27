rows, cols = tuple(map(int, input().split()))
matrix = [input().split() for i in range(rows)]
biggest_square = []
biggest_square_sum = 0


for row in range(rows - 2):
    for col in range(cols - 2):
        square = [
            [int(matrix[row][col]), int(matrix[row][col + 1]), int(matrix[row][col + 2])],
            [int(matrix[row + 1][col]), int(matrix[row + 1][col + 1]), int(matrix[row + 1][col + 2])],
            [int(matrix[row + 2][col]), int(matrix[row + 2][col + 1]), int(matrix[row + 2][col + 2])],
        ]
        square_sum = sum(sum(square, []))
        if square_sum > biggest_square_sum:
            biggest_square_sum = square_sum
            biggest_square = square

print(f'Sum = {biggest_square_sum}')
for x in biggest_square:
    print(" ".join(str(i) for i in x))
