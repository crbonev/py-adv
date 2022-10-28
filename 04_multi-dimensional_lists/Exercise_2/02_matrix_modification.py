size = int(input())

matrix = [[int(n) for n in input().split()] for _ in range(size)]
command = input().split()

while command[0] != 'END':
    cmd, row, col, num = command[0], int(command[1]), int(command[2]), int(command[3])
    if row < 0 or row >= size or col < 0 or col >= size:
        print('Invalid coordinates')
    elif cmd == 'Add':
        matrix[row][col] += num
    elif cmd == 'Subtract':
        matrix[row][col] -= num
    command = input().split()

for row in matrix:
    print(*row)