from piece import Bishop, Piece, Tower, Queen, Horse
from snake import Snake

class GameState:
        __board = [[]]
        __snake_c = 0
        __snake_l = 0

        def __init__(self):
                __board = [
                        [None, None, None, None, None],
                        [None, None, None, None, None],
                        [None, None, Queen(2, 2, 5, 5), None, None],
                        [1,   1, None, None, None],
                        [Snake, None, None, None, None]
                        ]
                
        
        def up(self): 
                if ( self.__snake_pos[0] > 0 ): return 0

                if (self.__snake_l + 1 < len( self.__board ):
                if (self.__board[self.__snake_c][self.__snake_l] )





if (board[2][2] is not None):
    board[2][2].printAttack()