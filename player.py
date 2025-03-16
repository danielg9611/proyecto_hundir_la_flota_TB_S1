import numpy as np
import random, time
from utils import print_boards


class Player ():
    def __init__(self, user=True):
        self.board = np.full((10,10), '_')
        self.user = user
        self.life = 16
        self.ship_list = []
        self.lasthit = None
        self.next_shot_direction = None
        self.create_random_ship(2)
        self.create_random_ship(2)
        self.create_random_ship(2)
        self.create_random_ship(3)
        self.create_random_ship(3)
        self.create_random_ship(4)
        self.set_all_ships()


    def set_all_ships(self):
        if self.user == True:
            for ship in self.ship_list:
                for coord in ship:
                    self.board[coord] = 'O'

    
    def got_shot_at(self, coordenates):

        for ship in self.ship_list:
            if coordenates in ship:
                self.board[coordenates] = "X"
                print('HIT')
                self.life -= 1
                if self.check_ship_destroyed(ship):
                    for coord in ship:
                        self.board[coord] = 'Z'

                return True
            else:
                self.board[coordenates] = 'A'
        print('MISS')


    def create_random_ship(self, size):

        
        is_valid = False

        while not is_valid:
            ship = []
            is_valid = True

            x = random.choice(range(0,10))
            y = random.choice(range(0,10))

            ship.append((x,y))

            direction = random.choice(['horizontal','vertical'])

            if direction == 'horizontal' and x + size-1 < 10:
                while len(ship) < size:
                    x+=1
                    ship.append((x,y))
            elif direction == 'horizontal' and x - size-1 >= 0:
                while len(ship) < size:
                    x-=1
                    ship.append((x,y))
            elif direction == 'vertical' and y + size-1  < 10:
                while len(ship) < size:
                    y+=1
                    ship.append((x,y))
            elif direction == 'vertical' and y - size-1 >= 0:
                while len(ship) < size:
                    y-=1
                    ship.append((x,y))

            for setted_ship in self.ship_list:
                for setted_ship_part in setted_ship:
                    if setted_ship_part in ship:
                        is_valid = False
                        continue

        self.ship_list.append(ship)


    def check_ship_destroyed(self, ship):
        solution = False
        for coord in ship:
            if self.board[coord] != 'X' and self.board[coord] != 'Z':
                solution = False
                break
            else:
                solution = True
        return solution
    

    def next_shot(self,player, direction = None):
        """
        Si el barco del ultimo disparo no ha sido destruido, dispara, la prrimera vez a una casilla adyacente random, la segunda vez a la casilla adyacente en la direccion del ultimo disparo

        La funcion devuelve las coordenadas de la casilla a disparar y la direccion del siguiente disparo

        Si el barco esta destruido, la funcion devuelve None y resetea las variables lasthit y next_shot_direction
        """
        for ship in player.ship_list:
            if self.lasthit in ship:
                
                while not player.check_ship_destroyed(ship):
                    x =  self.lasthit[0]
                    y =  self.lasthit[1]

                    if direction == None:
                        direction = random.choice(['up','down','left','right'])
                    else :
                        direction = direction
                    print(direction)
                    match direction:
                        case 'left':
                            if y > 0 and player.board[(x,y-1)] == 'O' and player.board[(x,y-1)] != '_':
                                y -= 1
                                print(x,y, 'left')
                            else:
                                direction = None  
                                continue
                        case 'right':
                            if y < 9 and player.board[(x,y+1)] == 'O' and player.board[(x,y+1)] == '_':
                                y += 1
                                print(x,y, 'rigth')
                            else:
                                direction = None
                                continue
                        case 'up':
                            if x > 0 and player.board[(x-1,y)] == 'O' and player.board[(x-1,y)] == '_':
                                x -= 1
                                print(x,y, 'up')
                            else:
                                direction = None
                                continue
                        case 'down':
                            if x < 9 and player.board[(x+1,y)] == 'O' and player.board[(x+1,y)] == '_':
                                x += 1
                                print(x,y, 'down')
                            else:
                                direction = None
                                continue

                    self.next_shot_direction = direction

                    return (x,y)
                
                if player.check_ship_destroyed(ship):
                    self.lasthit = None
                    self.next_shot_direction = None
                    return None

        self.next_shot_direction = None
        return None


    def shoot_at(self, player, board_player, board_pc, coord = None):

        if coord == None:

            coordenates = (random.choice(range(10)), random.choice(range(10)))
            
            if self.user == True:
                try:
                    coordenates = input('Escribe las coordenadas a donde quieres disparar ej.(1,1) : ')
                    coordenates = coordenates.replace('(', '').replace(')','').replace('.',',').split(',')
                    for i in range(2):
                        coordenates[i] = int(coordenates[i]) - 1
                        coordenates[i] = max(0, min(coordenates[i], 9))

                    coordenates = tuple(coordenates[::-1])
                except:
                    print("ERROR EN EL INPUT. SOLO SE ACEPTAN VALORES DE : X,Y o (X,Y)")
                    print("INTENTALO DE NUEVO")
                    self.shoot_at(player, board_player, board_pc, coord)
                    return

            elif self.user == False:
                if self.lasthit != None:
                    coordenates = self.next_shot(player, direction=self.next_shot_direction)
                else:
                    while player.board[coordenates] == 'X' or player.board[coordenates] == 'A':
                        x = random.choice(range(10))
                        y = random.choice(range(10))
                        coordenates = (x,y)

            if player.got_shot_at(coordenates):
                print_boards(board_player,board_pc)
                time.sleep(1.5)
                if player.life == 0:
                    return
                if self.user == True:
                    print('Tienes otro tiro, intentalo de nuevo')
                    self.shoot_at(player, board_player, board_pc, coord)
                elif self.user == False:
                    self.lasthit = coordenates
                    self.shoot_at(player, board_player, board_pc, self.next_shot(player, direction=self.next_shot_direction))

        else:
            if player.got_shot_at(coord):
                print_boards(board_player,board_pc)
                time.sleep(1.5)
                if player.life == 0:
                    return
                if self.user == False:
                    self.lasthit = coord
                    self.shoot_at(player, board_player, board_pc, self.next_shot(player, direction=self.next_shot_direction))
            else:
                self.next_shot_direction = None
                # self.lasthit = None 