import numpy as np
import random


class Player ():
    def __init__(self, user=True):
        self.board = np.full((10,10), '_')
        self.user = user
        self.life = 16
        self.ship_list = []
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
                        print('they join')
                        is_valid = False
                        continue

        self.ship_list.append(ship)

    def check_ship_destroyed(self, ship):
        solution = False
        for coord in ship:
            if self.board[coord] != 'X':
                solution = False
                break
            else:
                solution = True
        return solution


