rows, cols = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    if 'swap' not in command or len(command) != 5:
        print('Invalid input!')
        continue

    points = list(map(int, command[1:]))
    if points[0] > rows or points[1] > cols or \
            points[2] > rows or points[3] > cols:
        print('Invalid input!')
        continue

    points = list(map(int, command[1:]))
    p1, p2 = matrix[points[0]][points[1]], matrix[points[2]][points[3]]
    matrix[points[0]][points[1]] = p2
    matrix[points[2]][points[3]] = p1
    for row in matrix:
        print(*row)