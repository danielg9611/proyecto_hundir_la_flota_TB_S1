import random


def print_boards(board_player,board_pc):
    print('\n')
    print(f'------------------PLAYER-----------------', ' \t\t', f'----------------COMPUTER-----------------')
    for i in range(len(board_player)):
        print(board_player[i], '\t\t', board_pc[i])
    print(f'-----------------------------------------', ' \t\t', f'-----------------------------------------')


def shoot_at(player):

    coordenates = (random.choice(range(10)), random.choice(range(10)))
    
    if player.user == False:
        coordenates = input('Escribe las coordenadas a donde quieres disparar ej.(0,0) : ')
        coordenates = coordenates.replace('(', '').replace(')','').split(',')
        for i in range(2):
            coordenates[i] = int(coordenates[i]) - 1
            coordenates[i] = max(0, min(coordenates[i], 9))

        coordenates = tuple(coordenates[::-1])

    elif player.user == True:
        while player.board[coordenates] is 'X' or player.board[coordenates] is 'A':
            x = random.choice(range(10))
            y = random.choice(range(10))
            coordenates = (x,y)

    if player.got_shot_at(coordenates):
        if player.user == False:
            print('Tienes otro tiro, intentalo de nuevo')
        shoot_at(player)
    