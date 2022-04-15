from piece import King, Bishop, Tower, Queen, Horse, King
from snake import Snake
from gui import GUI
from utils import Action
import numpy as np

class GameState:
        
    __size = 0
    __piece_list = []

    def __init__(self, size, pieces):
        self.gui = GUI()
        self.__size = size

        self.snake = Snake(self.__size)

        self.__board = np.full([size, size], None)

        self.setPieces( pieces)

    def getSnake(self):
            return self.snake

    def getPieces(self):
            return self.__piece_list
    def getSize(self):
            return self.__size

    def setPieces(self, pieces):

        positions = []
                
        for piece_info in pieces:
                print(piece_info[0])
                if (piece_info[0] == 'H'):
                        curr_piece = Horse(piece_info[1], piece_info[2], self.__size)
                elif (piece_info[0] == 'Q'):
                        curr_piece = Queen(piece_info[1], piece_info[2], self.__size)
                elif (piece_info[0] == 'T'):
                        curr_piece = Tower(piece_info[1], piece_info[2], self.__size)
                elif (piece_info[0] == 'B'):
                        curr_piece = Bishop(piece_info[1], piece_info[2], self.__size)
                elif (piece_info[0] == 'K'):
                        curr_piece = King(piece_info[1], piece_info[2], self.__size)

                positions.append([piece_info[1], piece_info[2]])
                self.__piece_list.append( curr_piece)
                self.__board[piece_info[2]][piece_info[1]] = curr_piece
        
        for piece in self.__piece_list:
                piece.setAttack(positions)
                piece.printAttack()
        
    def evalMove(self, move, snake):
        if (move == Action.DOWN):
            if (self.__board[snake.getLine()+1][snake.getCol()] == None):
                return 1
            return 0
        if (move == Action.UP):
            if (self.__board[snake.getLine()-1][snake.getCol()] == None):
                return 1
            return 0
        if (move == Action.RIGHT):
            if (self.__board[snake.getLine()][snake.getCol()+1] == None):
                return 1
            return 0
        if (move == Action.LEFT):
            if (self.__board[snake.getLine()][snake.getCol()-1] == None):
                return 1
            return 0
        
    def checkPiecesNearby(self):
        vec = []
        if self.snake.getLine()+1 < self.__size:
                if (self.__board[self.snake.getLine()+1][self.snake.getCol()] != None):
                        vec.append(Action.DOWN)
        if self.snake.getLine()-1 >= 0:
                if (self.__board[self.snake.getLine()-1][self.snake.getCol()] != None):
                        vec.append(Action.UP)
        if self.snake.getCol()+1 < self.__size:
                if (self.__board[self.snake.getLine()][self.snake.getCol()+1] != None):
                        vec.append(Action.RIGHT)
        if self.snake.getCol()-1 >= 0:
                if (self.__board[self.snake.getLine()][self.snake.getCol()-1] != None):
                        vec.append(Action.LEFT)
        return vec

    def countAttacks(self, snake): 
        snake_bitmap = snake.getBitmap()
        curr_num = self.__piece_list[0].AttackNum(snake_bitmap)

        for piece in self.__piece_list:
            num_attacks = piece.AttackNum( snake_bitmap)
            if ( curr_num != num_attacks):
                    return 0
        return 1
            
