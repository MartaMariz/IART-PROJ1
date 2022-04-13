from utils import Action
import numpy as np

class Snake:
    def __init__(self, size):
        self.board_size = size
        self.pos = [size-1, 0]
        self.bitmap = np.array([[0]*(size)]*(size))
        self.bitmap[self.pos[0]][self.pos[1]] = 1
        print(self.bitmap)
        
    def up(self): 
        if self.pos[0] <= 0: return 0
        if self.bitmap[self.pos[0]-1][self.pos[1]]: return 0
        if (self.pos[0]-1 >= 0):
            if (self.pos[1]-1 >= 0):
                if (self.bitmap[self.pos[0]-1][self.pos[1]-1]):
                    print("here")
                    return 0
            if (self.pos[1]+1 <= self.board_size-1):
                if(self.bitmap[self.pos[0]-1][self.pos[1]+1]):
                    print("there")
                    return 0
            print("na boa")
        if (self.pos[0]-2 >= 0):
            if (self.pos[1]-1 >= 0):
                if (self.bitmap[self.pos[0]-2][self.pos[1]-1]):
                    print("there2")
                    return 0
            if (self.pos[1]+1 <= self.board_size-1):
                if(self.bitmap[self.pos[0]-2][self.pos[1]+1]):
                    print("there3")
                    return 0
            print("na boa2")
            return 1 
        return 1

    def down(self): 
        if self.pos[0] >= self.board_size-1: return 0
        if self.bitmap[self.pos[0]+1][self.pos[1]]: return 0
        if (self.pos[0]+1 <= self.board_size-1):
            if (self.pos[1]-1 >= 0):
                if (self.bitmap[self.pos[0]+1][self.pos[1]-1]):
                    print("here")
                    return 0
            if (self.pos[1]+1 <= self.board_size-1):
                if(self.bitmap[self.pos[0]+1][self.pos[1]+1]):
                    print("there")
                    return 0
            print("na boa")
        if (self.pos[0]+2 <= self.board_size-1):
            if (self.pos[1]-1 >= 0):
                if (self.bitmap[self.pos[0]+2][self.pos[1]-1]):
                    print("there2")
                    return 0
            if (self.pos[1]+1 <= self.board_size-1):
                if(self.bitmap[self.pos[0]+2][self.pos[1]+1]):
                    print("there3")
                    return 0
            print("na boa2")
            return 1
        return 1

    def left(self): 
        if self.pos[1] <= 0: return 0
        if self.bitmap[self.pos[0]][self.pos[1]-1]: return 0
        if (self.pos[1]-1 >= 0):
            if (self.pos[0]-1 >= 0):
                if (self.bitmap[self.pos[0]-1][self.pos[1]-1]):
                    print("here")
                    return 0
            if (self.pos[0]+1 <= self.board_size-1):
                if(self.bitmap[self.pos[0]+1][self.pos[1]-1]):
                    print("there")
                    return 0
            print("na boa")
        if (self.pos[1]-2 >= 0):
            if (self.pos[0]-1 >= 0):
                if (self.bitmap[self.pos[0]-1][self.pos[1]-2]):
                    print("there2")
                    return 0
            if (self.pos[0]+1 <= self.board_size-1):
                if(self.bitmap[self.pos[0]+1][self.pos[1]-2]):
                    print("there3")
                    return 0
            print("na boa2")
            return 1  
        return 1

    def right(self): 
        if self.pos[1] >= self.board_size-1: return 0
        if self.bitmap[self.pos[0]][self.pos[1]+1]: return 0
        if (self.pos[1]+1 <= self.board_size-1):
            if (self.pos[0]-1 >= 0):
                if (self.bitmap[self.pos[0]-1][self.pos[1]+1]):
                    print("here")
                    return 0
            if (self.pos[0]+1 <= self.board_size-1):
                if(self.bitmap[self.pos[0]+1][self.pos[1]+1]):
                    print("there")
                    return 0
            print("na boa")
        if (self.pos[1]+2 <= self.board_size-1):
            if (self.pos[0]-1 >= 0):
                if (self.bitmap[self.pos[0]-1][self.pos[1]+2]):
                    print("there2")
                    return 0
            if (self.pos[0]+1 <= self.board_size-1):
                if(self.bitmap[self.pos[0]+1][self.pos[1]+2]):
                    print("there3")
                    return 0
            print("na boa2")
            return 1
        return 1

    def checkPossibleMoves(self, pieces):
        if self.up() and not Action.UP in pieces:
            return 1
        if self.down() and not Action.DOWN in pieces:
            return 1
        if self.left() and not Action.LEFT in pieces:
            return 1
        if self.right() and not Action.RIGHT in pieces:
            return 1
        return 0

    def updateSnake(self, move):
        if (move == Action.DOWN):
            self.bitmap[self.pos[0]+1][self.pos[1]] = 1
            self.pos[0] += 1
        if (move == Action.UP):
            self.bitmap[self.pos[0]-1][self.pos[1]] = 1
            self.pos[0] -= 1
        if (move == Action.RIGHT):
            self.bitmap[self.pos[0]][self.pos[1]+1] = 1
            self.pos[1] += 1
        if (move == Action.LEFT):
            self.bitmap[self.pos[0]][self.pos[1]-1] = 1
            self.pos[1] -= 1

    def endGame(self):
        if self.pos[0] == self.board_size-1 and self.pos[1] == self.board_size-1: 
            print("tf")
            return 1
        return 0