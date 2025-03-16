import time, art
from player import Player
from utils import *



def juego():

    player = Player()
    pc = Player(user=False)

    print(art.art)
    print("\tBIENVENIDO A HUNDIR LA FLOTA")
    print("\tES TU TURNO")
    print_boards(player.board,pc.board)    

    while player.life > 0 and pc.life > 0:

        ### DEBUG ###

        # print(pc.ship_list)

        #############


        ### PLAYER TURN ###
        
        player.shoot_at(pc, player.board,pc.board)
        print()
        time.sleep(.5)
        print_boards(player.board,pc.board)   
        print()
        time.sleep(1)
        if pc.life == 0:
            break

        ### PC TURN ###

        print('TURNO DEL OPONENTE')
        print('pensando...')
        print()
        time.sleep(2)
        pc.shoot_at(player, player.board,pc.board)
        print()
        print_boards(player.board,pc.board)   
        print()
    
    if player.life == 0:
        print('HAS PERDIDO, MAS SUERTE EN LA PROXIMA')
    elif pc.life == 0:
        print('HAS GANADO!!!')

    volver_a_jugar = input('Quiere volver a jugar?  [Y/N]\n')

    if volver_a_jugar.lower() == 'y' or volver_a_jugar.lower() == 'yes':
        juego()

juego()