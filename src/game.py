from piece import Bishop, Tower, Queen, Horse
from snake import Snake
from gui import GUI
from utils import Action
import numpy as np

class GameState:
    __size = 5
        
    def __init__(self):
        self.gui = GUI()
        self.snake = Snake(self.__size)
        tower = Tower(2, 2, 5, 5)
        bishop = Bishop(1, 0, 5, 5)
        horse = Horse(3, 2, 5, 5)
        vec = [tower, bishop, horse]
        #queen.setAttacks(bishop.position, horse.position)
        self.__board = np.array([
                [None, bishop, None, None, None],
                [None, None, None, None, None],
                [None, None, tower, horse, None],
                [None,   None, None, None, None],
                [self.snake, None, None, None, None]
                ])
        
        self.game(vec)
        
    def evalMove(self, move):
        if (move == Action.DOWN):
            if (self.__board[self.snake.pos[0]+1][self.snake.pos[1]] == None):
                return 1
            return 0
        if (move == Action.UP):
            if (self.__board[self.snake.pos[0]-1][self.snake.pos[1]] == None):
                return 1
            return 0
        if (move == Action.RIGHT):
            if (self.__board[self.snake.pos[0]][self.snake.pos[1]+1] == None):
                return 1
            return 0
        if (move == Action.LEFT):
            if (self.__board[self.snake.pos[0]][self.snake.pos[1]-1] == None):
                return 1
            return 0
        
    def checkPiecesNearby(self):
        vec = []
        if self.snake.pos[0]+1 < self.__size:
                if (self.__board[self.snake.pos[0]+1][self.snake.pos[1]] != None):
                        vec.append(Action.DOWN)
        if self.snake.pos[0]-1 >= 0:
                if (self.__board[self.snake.pos[0]-1][self.snake.pos[1]] != None):
                        vec.append(Action.UP)
        if self.snake.pos[1]+1 < self.__size:
                if (self.__board[self.snake.pos[0]][self.snake.pos[1]+1] != None):
                        vec.append(Action.RIGHT)
        if self.snake.pos[1]-1 >= 0:
                if (self.__board[self.snake.pos[0]][self.snake.pos[1]-1] != None):
                        vec.append(Action.LEFT)
        return vec

    def game(self, vec):
        inGame = True
        while(inGame):
            if self.snake.endGame():
                print("the game is over!")
                inGame = False
            pieces = self.checkPiecesNearby()
            print(pieces)
            if not self.snake.checkPossibleMoves(pieces):
                print("you lost the game!")
                inGame = False
            nextAction = self.gui.showboard(self.__size, vec, self.snake)
            if nextAction == Action.QUIT:
                print("bye!")
                inGame = False
            else:
                if (self.evalMove(nextAction)):
                    self.snake.updateSnake(nextAction)
            
            
            
            


