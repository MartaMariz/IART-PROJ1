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
        if (self.pos[0] <= 0): return 0
        #if (self.pos[0] + 1 < len(self.board_size)): return 0
        else: return 1
    def down(self): 
        if (self.pos[0] >= self.board_size-1): return 0
        else: return 1
    def left(self): 
        if (self.pos[1] <= 0): return 0
        #if (self.pos[0] + 1 < len(self.board_size)): return 0
        else: return 1
    def right(self): 
        if (self.pos[1] >= self.board_size-1): return 0
        else: return 1    

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