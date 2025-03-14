import time, art
from player import Player
from utils import *


player = Player()
pc = Player(user=False)

print(pc.ship_list)
def juego():
    player.life = 16
    pc.life = 16
    print(art.art)
    print("\tBIENVENIDO A HUNDIR LA FLOTA")
    print("\tES TU TURNO")
    print_boards(player.board,pc.board)    

    while player.life > 0 and pc.life > 0:

        ### PLAYER TURN ###

        shoot_at(pc)
        print()
        print_boards(player.board,pc.board)   
        print()
        time.sleep(1)


        ### PC TURN ###

        print('TURNO DEL OPONENTE')
        print('pensando...')
        print()
        time.sleep(2)
        shoot_at(player)
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


## TODO: Imprimir la tabla despues de cada disparo del jugador

## TODO: Hacer que la maquina tenga una logica de juego [si el disparo es hit disparar a las casillas adjacentes]