from piece import Bishop, Tower, Queen, Horse
from snake import Snake
from gui import GUI


class GameState:
        __board = [[]]
        __size = 5
        __snake_c = 0
        __snake_l = 0
        print("hello")
        
        
        def __init__(self):
                self.gui = GUI()
                tower = Tower(2, 2, 5, 5)
                bishop = Bishop(1, 0, 5, 5)
                horse = Horse(3, 2, 5, 5)
                vec = [tower, bishop, horse]
                #queen.setAttacks(bishop.position, horse.position)
                __board = [
                        [None, None, None, None, None],
                        [None, None, None, None, None],
                        [None, None, tower, None, None],
                        [1,   1, None, None, None],
                        [Snake, None, None, None, None]
                        ]
                
                self.game(vec)
                
        def game(self, vec):
                self.gui.showboard(self.__size, vec)
        
        def up(self): 
                if ( self.__snake_pos[0] > 0 ): return 0

                if (self.__snake_l + 1 < len( self.__board )): return 0

