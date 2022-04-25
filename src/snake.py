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
        """Cretes another object snake with the same attributes as the original, used to get nodes to be used in the search algorithms

        Args:
            snake (Snake): object snake whose attributes will be copied
        """
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

    def restartSnake(self):
        """Transforms the snake into its initial format
        """
        self.__pos = [self.board_size-1, 0]
        self.__bitmap = np.array([[0]*(self.board_size)]*(self.board_size))
        self.__bitmap[self.__pos[0]][self.__pos[1]] = 1
      
    def up(self): 
        """Checks if tho move up is possible

        Returns:
            int: 0 if it is not possible, 1 if it is
        """
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
        """Checks if tho move down is possible

        Returns:
            int: 0 if it is not possible, 1 if it is
        """
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
        """Checks if tho move left is possible

        Returns:
            int: 0 if it is not possible, 1 if it is
        """
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
        """Checks if tho move right is possible

        Returns:
            int: 0 if it is not possible, 1 if it is
        """
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
        """Checks if there is any possible movement taking into account the information of the main board

        Args:
            pieces (vector): vector of actions that encapsule what moves are possible taking only into account the chess piece's positions and the size of the board

        Returns:
            int: 1 if there are any 0 if not
        """
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
        """Heuristics to get the distance from the current position the end of the board

        Returns:
            int:  manhatan distance from the current position the end of the board
        """
        return self.__pos[0] + abs(self.__pos[1] - (self.board_size -1))

    def updateSnake(self, move):
        """Updates the snake with the move chosen

        Args:
            move (ACTION): move selected
        """
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
        """The function creates a new node with the information from the current snake and the operation provided

        Args:
            move (Action): operator, can be UP, DOWN, LEFT, RIGHT

        Returns:
            Snake: the resulting object snake
        """
        new_snake = Snake(self.board_size)
        new_snake.copy( self )
        new_snake.updateSnake(move)
       
        return new_snake

    def endGame(self):
        """Check if the snake is at the ending slot

        Returns:
        int: 1 if it is, 0 if not
        """
        if self.__pos[0] == 0 and self.__pos[1] == self.board_size-1: 
            return 1
        return 0

