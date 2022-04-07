from piece import Bishop, Piece, Tower, Queen, Horse
from snake import Snake
from gui import GUI

class GameState:
        __board = [[]]
        __snake_c = 0
        __snake_l = 0
        GUI()
        
        def __init__(self):
                queen = Queen(2, 2, 5, 5)
                bishop = Bishop(1, 0, 5, 5)
                horse = Horse(3, 2, 5, 5)
                queen.setAttacks(bishop.position, horse.position)
                __board = [
                        [None, None, None, None, None],
                        [None, None, None, None, None],
                        [None, None, queen, None, None],
                        [1,   1, None, None, None],
                        [Snake, None, None, None, None]
                        ]
                
        
        def up(self): 
                if ( self.__snake_pos[0] > 0 ): return 0

                if (self.__snake_l + 1 < len( self.__board )): return 0



