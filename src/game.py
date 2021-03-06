from piece import King, Bishop, Tower, Queen, Horse, King
from snake import Snake
from gui import GUI
from utils import Action
import numpy as np

class GameState:
        
    __size = 0
    __piece_list = []

    def __init__(self, size, pieces):
        """ Build game set up 

        Args:
        size (int): size of board number of collumns is equal to number of lines
        pieces (vector): specifies the piece type and its position in the board
        """
        self.gui = GUI()
        self.__size = size

        self.snake = Snake(self.__size)

        self.__board = np.full([size, size], 0)

        self.setPieces(pieces)

    def getSnake(self):
            return self.snake

    def getPieces(self):
            return self.__piece_list

    def getSize(self):
            return self.__size

    def restartSnake(self):
            self.snake.restartSnake()

    def setPieces(self, pieces):
        """ calls builds the pieces and saves them in a vector 

        Args:
        pieces (vector): string identifying  the piece type and ints identifying its position in the board
        """

        positions = []
        self.__piece_list.clear()
                
        for piece_info in pieces:
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
                self.__board[piece_info[2]][piece_info[1]] = 1
        
        for piece in self.__piece_list:
                piece.setAttack(positions)
        
    def evalMove(self, move, snake):
        """ checks if the move chosen is valid, if the snake doesn't go to a slot occupied

        Args:
        move (Action): move chosen by the player
        snake (Snake): snake object to evaluate

        Returns:
        int: 1 if the move is valid, 0 if it is not
        """
        if (move == Action.DOWN):
            if (self.__board[snake.getLine()+1][snake.getCol()] == 0):
                return 1
            return 0
        if (move == Action.UP):
            if (self.__board[snake.getLine()-1][snake.getCol()] == 0):
                return 1
            return 0
        if (move == Action.RIGHT):
            if (self.__board[snake.getLine()][snake.getCol()+1] == 0):
                return 1
            return 0
        if (move == Action.LEFT):
            if (self.__board[snake.getLine()][snake.getCol()-1] == 0):
                return 1
            return 0
        
    def checkPiecesNearby(self):
        """ evaluates the possible moves of the snake taking account the position of the pieces in the board

        Returns:
        vector: vector with the possible actions for the snake
        """
        vec = []
        if self.snake.getLine()+1 < self.__size:
                if (self.__board[self.snake.getLine()+1][self.snake.getCol()] != 0):
                        vec.append(Action.DOWN)
        if self.snake.getLine()-1 >= 0:
                if (self.__board[self.snake.getLine()-1][self.snake.getCol()] != 0):
                        vec.append(Action.UP)
        if self.snake.getCol()+1 < self.__size:
                if (self.__board[self.snake.getLine()][self.snake.getCol()+1] != 0):
                        vec.append(Action.RIGHT)
        if self.snake.getCol()-1 >= 0:
                if (self.__board[self.snake.getLine()][self.snake.getCol()-1] != 0):
                        vec.append(Action.LEFT)
        return vec

    def countAttacks(self, snake): 
        """ checks if all the pieces have the same number of attacks therefor if the player won or lost the game

        Args:
        snake (Snake): snake to evaluate

        Returns:
        int: 1 if the player won, 0 if not
        """
        snake_bitmap = snake.getBitmap()
        curr_num = self.__piece_list[0].AttackNum(snake_bitmap)

        for piece in self.__piece_list:
            num_attacks = piece.AttackNum( snake_bitmap)
            if ( curr_num != num_attacks):
                    return 0
        return 1

    def getAbsDifAttacks( self, snake):
        """ Heuristics evaluating the difference of the number of times a piece attacks snake segments 

        Args:
        snake (Snake): snake to evaluate

        Returns:
        int: absolute of the difference between the number of attacks of the piece with the most attacks and the piece with least
        """
        snake_bitmap = snake.getBitmap()
        if (self.__size == 5):
            return abs( self.__piece_list[0].AttackNum( snake_bitmap) - self.__piece_list[1].AttackNum( snake_bitmap) )

        else:
            max_attacks = -1
            min_attacks = self.__piece_list[0].AttackNum( snake_bitmap)

            for piece in self.__piece_list:
                curr_attacks = piece.AttackNum( snake_bitmap)
                if ( curr_attacks > max_attacks):
                        max_attacks = curr_attacks
                elif ( curr_attacks < min_attacks):
                        min_attacks = curr_attacks
        
        return abs(max_attacks - min_attacks)

                                 
