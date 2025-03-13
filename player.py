import numpy as np
import random


class Player ():
    def __init__(self):
        self.board = np.full((10,10), '_')
        self.create_random_ship(3)
        self.create_random_ship(3)
        self.ship_list = []
    
    def ship_set(self,coordenates:list):
        '''Coloca el barco (lista de coordenadas) en la tabla'''
        for coord in coordenates:
            self.board[coord] = 'O'

    
    def got_shot_at(self, coordenates):
        if self.board[coordenates] == 'O':
            print('Hit')
            self.board[coordenates] = 'X'
        else:
            print('Miss')
            self.board[coordenates] = 'M'


    def create_random_ship(self, size):
        ship = []

        x = random.choice(range(0,10))
        y = random.choice(range(0,10))
        coordinates = (y,x)

        ship.append(coordinates)

        direction = random.choice(['horizontal','vertical'])

        if direction == 'horizontal' and x + size-1 < 10:
            while len(ship) < size:
                x+=1
                ship.append((y,x))
        elif direction == 'horizontal' and x - size-1 >= 0:
            while len(ship) < size:
                x-=1
                ship.append((y,x))
        elif direction == 'vertical' and y + size-1  < 10:
            while len(ship) < size:
                y+=1
                ship.append((y,x))
        elif direction == 'vertical' and y - size-1 >= 0:
            while len(ship) < size:
                y-=1
                ship.append((y,x))

        print(ship)

        self.ship_set(ship)

    def create_set_ship_list(self):
        pass

