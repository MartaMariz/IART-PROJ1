from piece import Bishop, Tower, Queen, Horse
from snake import Snake
from gui import GUI
from utils import Action


class GameState:
        __board = [[]]
        __size = 5
        
        def __init__(self):
                self.gui = GUI()
                self.snake = Snake(self.__size)
                tower = Tower(2, 2, 5, 5)
                bishop = Bishop(1, 0, 5, 5)
                horse = Horse(3, 2, 5, 5)
                vec = [tower, bishop, horse]
                #queen.setAttacks(bishop.position, horse.position)
                __board = [
                        [None, None, None, None, None],
                        [None, None, None, None, None],
                        [None, None, tower, None, None],
                        [None,   None, None, None, None],
                        [Snake, None, None, None, None]
                        ]
                
                self.game(vec)
        
        #def evalMove(self, move):


        def game(self, vec):
                inGame = True
                while(inGame):
                        nextAction = self.gui.showboard(self.__size, vec, self.snake)
                        if nextAction == Action.QUIT:
                                print("bye!")
                                inGame = False
                        else: self.snake.updateSnake(nextAction)
