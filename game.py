def play(matrix, turn):
    if turn % 2 == 0:
        result = 2
    else:
        result = 1
    column = input(f'Player {result} enter column: ')
    try:
        column = int(column)
        for x in range(6, 0, -1):
            if matrix[x - 1][column - 1] == 0:
                matrix[x - 1][column - 1] = result
                break
    except IndexError:
        print('Invalid column')
        play(matrix, turn)
    except ValueError:
        print('Invalid column')
        play(matrix, turn)


def print_matrix(matrix):
    for row in matrix:
        print(row)


def player_win(matrix):
    for player in range(1, 2 + 1):
        for i, r in enumerate(matrix):
            for idx, el in enumerate(r):
                try:
                    if matrix[i][idx] == matrix[i][idx + 1] == matrix[i][idx + 2] == matrix[i][idx + 3] != 0:
                        print(f'Player no.: {player} wins')
                        return True
                    if matrix[i][idx] == matrix[i - 1][idx] == matrix[i - 2][idx] == matrix[i - 3][idx] != 0:
                        print(f'Player no.: {player} wins')
                        return True
                    if matrix[i][idx] == matrix[i - 1][idx + 1] == matrix[i - 2][idx + 2] == matrix[i - 3][idx + 3] != 0:
                        print(f'Player no.: {player} wins')
                        return True
                    if matrix[i][idx] == matrix[i - 1][idx - 1] == matrix[i - 2][idx - 2] == matrix[i - 3][idx - 3] != 0:
                        print(f'Player no.: {player} wins')
                        return True
                except IndexError:
                    continue


play_field = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

player_turn = 1
while True:

    win = False
    play(play_field, player_turn)

    player_turn += 1

    print_matrix(play_field)

    if player_win(play_field):
        win = True
        break


