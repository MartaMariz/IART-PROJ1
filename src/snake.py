from utils import Action
import numpy as np

class Snake:
    def __init__(self, size):
        self.board_size = size
        self.__pos = [size-1, 0]
        self.__bitmap = np.array([[0]*(size)]*(size))
        self.__bitmap[self.__pos[0]][self.__pos[1]] = 1
        self.__cost = 0
    
    def copy(self, snake):
        self.__bitmap = snake.getBitmap()
        self.__cost = snake.__cost + 1
        self.__pos[0] = snake.getLine()
        self.__pos[1] = snake.getCol()
    
    def getBitmap(self):
        return self.__bitmap.copy()
    
    def getCost(self):
        return self.__cost
    
    def getBoardSize(self):
        return self.board_size
    
    def getLine(self):
        return self.__pos[0]
    
    def getCol(self):
        return self.__pos[1]

    def isOcupied(self, l, c):
        return self.__bitmap[l][c]
      
    def up(self): 
        if self.__pos[0] <= 0: return 0
        if self.__bitmap[self.__pos[0]-1][self.__pos[1]]: return 0
        if (self.__pos[0]-1 >= 0):
            if (self.__pos[1]-1 >= 0):
                if (self.__bitmap[self.__pos[0]-1][self.__pos[1]-1]):
                    return 0
            if (self.__pos[1]+1 <= self.board_size-1):
                if(self.__bitmap[self.__pos[0]-1][self.__pos[1]+1]):
                    return 0
        if (self.__pos[0]-2 >= 0):
            if (self.__pos[1]-1 >= 0):
                if (self.__bitmap[self.__pos[0]-2][self.__pos[1]-1]):
                    return 0
            if (self.__pos[1]+1 <= self.board_size-1):
                if(self.__bitmap[self.__pos[0]-2][self.__pos[1]+1]):
                    return 0
            return 1 
        return 1

    def down(self): 
        if self.__pos[0] >= self.board_size-1: return 0
        if self.__bitmap[self.__pos[0]+1][self.__pos[1]]: return 0
        if (self.__pos[0]+1 <= self.board_size-1):
            if (self.__pos[1]-1 >= 0):
                if (self.__bitmap[self.__pos[0]+1][self.__pos[1]-1]):
                    return 0
            if (self.__pos[1]+1 <= self.board_size-1):
                if(self.__bitmap[self.__pos[0]+1][self.__pos[1]+1]):
                    return 0
        if (self.__pos[0]+2 <= self.board_size-1):
            if (self.__pos[1]-1 >= 0):
                if (self.__bitmap[self.__pos[0]+2][self.__pos[1]-1]):
                    return 0
            if (self.__pos[1]+1 <= self.board_size-1):
                if(self.__bitmap[self.__pos[0]+2][self.__pos[1]+1]):
                    return 0
            return 1
        return 1

    def left(self): 
        if self.__pos[1] <= 0: return 0
        if self.__bitmap[self.__pos[0]][self.__pos[1]-1]: return 0
        if (self.__pos[1]-1 >= 0):
            if (self.__pos[0]-1 >= 0):
                if (self.__bitmap[self.__pos[0]-1][self.__pos[1]-1]):
                    return 0
            if (self.__pos[0]+1 <= self.board_size-1):
                if(self.__bitmap[self.__pos[0]+1][self.__pos[1]-1]):
                    return 0
        if (self.__pos[1]-2 >= 0):
            if (self.__pos[0]-1 >= 0):
                if (self.__bitmap[self.__pos[0]-1][self.__pos[1]-2]):
                    return 0
            if (self.__pos[0]+1 <= self.board_size-1):
                if(self.__bitmap[self.__pos[0]+1][self.__pos[1]-2]):
                    return 0
            return 1  
        return 1

    def right(self): 
        if self.__pos[1] >= self.board_size-1: return 0
        if self.__bitmap[self.__pos[0]][self.__pos[1]+1]: return 0
        if (self.__pos[1]+1 <= self.board_size-1):
            if (self.__pos[0]-1 >= 0):
                if (self.__bitmap[self.__pos[0]-1][self.__pos[1]+1]):
                    return 0
            if (self.__pos[0]+1 <= self.board_size-1):
                if(self.__bitmap[self.__pos[0]+1][self.__pos[1]+1]):
                    return 0
        if (self.__pos[1]+2 <= self.board_size-1):
            if (self.__pos[0]-1 >= 0):
                if (self.__bitmap[self.__pos[0]-1][self.__pos[1]+2]):
                    return 0
            if (self.__pos[0]+1 <= self.board_size-1):
                if(self.__bitmap[self.__pos[0]+1][self.__pos[1]+2]):
                    return 0
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

    def getDistancetoEnd(self):
        return self.__pos[0] + abs(self.__pos[1] - (self.board_size -1))

    def updateSnake(self, move):
        if (move == Action.DOWN):
            self.__bitmap[self.__pos[0]+1][self.__pos[1]] = 1
            self.__pos[0] += 1
        if (move == Action.UP):
            self.__bitmap[self.__pos[0]-1][self.__pos[1]] = 1
            self.__pos[0] -= 1
        if (move == Action.RIGHT):
            self.__bitmap[self.__pos[0]][self.__pos[1]+1] = 1
            self.__pos[1] += 1
        if (move == Action.LEFT):
            self.__bitmap[self.__pos[0]][self.__pos[1]-1] = 1
            self.__pos[1] -= 1
    
    def getNewSnake(self, move):
        new_snake = Snake(self.board_size)
        new_snake.copy( self )
        new_snake.updateSnake(move)
       
                    
        #print(new_snake.getBitmap())
        return new_snake

    def endGame(self):
        if self.__pos[0] == 0 and self.__pos[1] == self.board_size-1: 
            return 1
        return 0

