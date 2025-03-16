import random, time

def print_boards(board_player,board_pc):
    print('\n')
    print(f'----------PLAYER----------', ' \t\t', f'---------COMPUTER---------')
    for i in range(10):
        print('|', end ='  ')
        for j in range(10):
            print(board_player[(i,j)], end=' ')
        print('  |', end='\t\t |  ')

        for j in range(10):
            print(board_pc[(i,j)], end=' ')
        print('  |')

        # print(board_player[i], '\t\t', board_pc[i])
    print(f'--------------------------', ' \t\t', f'--------------------------')



