from game import GameState
from utils import Action
import numpy as np


class BFS:
    def __init__(self, game):
        print("here")
        snake = game.getSnake()
        tree = np.array([ snake ])
        print(len(tree))

        i = 0

        while (1):
            print("here1")

            curr_snake = tree[0]
            tree = np.delete(tree,0)
            i+=1

            if ( curr_snake.endGame()):
                if (game.CountAttacks(curr_snake)): 
                    break
                else:
                    continue
            
            if ( curr_snake.up() and game.evalMove(Action.UP, curr_snake)): 
                new_snake = curr_snake.getNewSnake(Action.UP)
                tree = np.append(tree, new_snake)
            if ( curr_snake.down() and game.evalMove(Action.DOWN, curr_snake)): 
                new_snake = curr_snake.getNewSnake(Action.DOWN)
                tree = np.append(tree, new_snake)
            if ( curr_snake.left() and game.evalMove(Action.LEFT, curr_snake)): 
                new_snake = curr_snake.getNewSnake(Action.LEFT)
                tree = np.append(tree, new_snake)
            if ( curr_snake.right() and game.evalMove(Action.RIGHT, curr_snake)): 
                new_snake = curr_snake.getNewSnake(Action.RIGHT)
                tree = np.append(tree, new_snake)

        game.gui.showboard(game.getSize(), game.getPieces(), curr_snake)
