from re import S
from piece import Bishop, Piece, Tower, Queen, Horse
from snake import Snake

class Game:
        __pieces = []
        __board = [[]]
        __snake = 0

        def __init__(lines, cols, positions, self):

                self.init_board( lines, cols, positions)

                self.init_snake( lines, cols)

                for piece in positions:
                        if ( piece[0] == 'H'):
                                self.__pieces.append( Tower(lines, cols, positions))

        
        def up(self): 
                if ( self.__snake_pos[0] > 0 ): return 0

                if (self.__snake_l - 1 > 0 ): 
                        return 0
        
        def printBoard(self):
                if (self.__board[2][2] is not None):
                        self.__board[2][2].printAttack()


board = Game( 5, 5, ['H', 1, 3])
board.printBoard()





