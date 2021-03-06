from game import GameState
from utils import Action, ALGORITHM
import numpy as np
import time 
import shutil
path = "./src"
  

class Search:
    def __init__(self, game):
        """Prepares the necessary structures to perform the search

        Args:
            game (Game): game iniciated on main
        """
        self.__tree = np.array([ game.getSnake() ]) 
        self.__game = game
    
    def beginSearch(self, alg):
        """Executes the search

        Args:
            alg (ALGORITHM): specifies the algorithm that will be implemented

        Returns:
            Snake: the resulting snake
        """
        i = 0
        start = time.time()
        

        while (1):
            if len(self.__tree) == 0:
                return Action.LOST

            if (alg == ALGORITHM.BFS):
                curr_snake = self.bfs()
            elif (alg == ALGORITHM.UCOST):
                curr_snake = self.ucost()
            elif (alg == ALGORITHM.GS1):
                curr_snake = self.greedy1()
            elif (alg == ALGORITHM.As1):
                curr_snake = self.as1()
            elif (alg == ALGORITHM.As2):
                curr_snake = self.as2()


            i+=1

            if ( curr_snake.endGame()):
                if (self.__game.countAttacks(curr_snake)): 
                    break
                else:
                    continue
           
            if (curr_snake.up() and self.__game.evalMove(Action.UP, curr_snake)): 
                new_snake = curr_snake.getNewSnake(Action.UP)
                self.__tree = np.append(self.__tree, new_snake)
            if (curr_snake.down() and self.__game.evalMove(Action.DOWN, curr_snake)): 
                new_snake = curr_snake.getNewSnake(Action.DOWN)
                self.__tree = np.append(self.__tree, new_snake)
            if (curr_snake.left() and self.__game.evalMove(Action.LEFT, curr_snake)): 
                new_snake = curr_snake.getNewSnake(Action.LEFT)
                self.__tree = np.append(self.__tree, new_snake)
            if (curr_snake.right() and self.__game.evalMove(Action.RIGHT, curr_snake)): 
                new_snake = curr_snake.getNewSnake(Action.RIGHT)
                self.__tree = np.append(self.__tree, new_snake)

        print("Number of nodes explored: ", i)
        self.__tree = [ self.__game.getSnake()]

        end = time.time()
        print("Time of execution: ", end - start)
        print("Profundidade: ", curr_snake.getCost())

        stat = shutil.disk_usage(path)
        
        print("Disk usage statistics:")
        print(stat)

        return curr_snake

    def bfs(self):
        """Selects the next node to be explored according to the breadth first search algorithm

        Returns:
            Snake: new node which is the resulting snake
        """
        curr_snake = self.__tree[0]
        self.__tree = np.delete(self.__tree,0)

        return curr_snake
    
    def ucost(self):
        """Selects the next node to be explored according to the uniform cost algorithm

        Returns:
            Snake: new node which is the resulting snake
        """
        index = 0
        minhc = self.__tree[0].getCost()
        for i in range (1,len(self.__tree)):
            curr_hc = self.__tree[i].getCost()
            if( curr_hc <= minhc):
                index = i
                minhc = curr_hc

        curr_snake = self.__tree[index]            
        self.__tree = np.delete(self.__tree,index)

        return curr_snake
    
    def greedy1(self):
        """Selects the next node to be explored according to the greedy search algorithm with the manhatan distance to the end heuristic

        Returns:
            Snake: new node which is the resulting snake
        """
        index = 0
        minhc = self.__tree[0].getDistancetoEnd()
        for i in range (1,len(self.__tree)):
            curr_hc = self.__tree[i].getDistancetoEnd()
            if( curr_hc <= minhc):
                index = i
                minhc = curr_hc

        curr_snake = self.__tree[index]            
        self.__tree = np.delete(self.__tree,index)

        return curr_snake


    def as1(self):
        """Selects the next node to be explored according to the A* algorithm with the manhatan distance to the end heuristic

        Returns:
            Snake: new node which is the resulting snake
        """
        index = 0
        minhc = self.__tree[0].getDistancetoEnd() + self.__tree[0].getCost()
        for i in range (1,len(self.__tree)):
            curr_hc = self.__tree[i].getDistancetoEnd() + self.__tree[i].getCost()
            if( curr_hc <= minhc):
                index = i
                minhc = curr_hc

        curr_snake = self.__tree[index]            
        self.__tree = np.delete(self.__tree,index)

        return curr_snake

    def as2(self):
        """Selects the next node to be explored according to the A* algorithm with absolute of the difference between the number of attacks heuristic

        Returns:
            Snake: new node which is the resulting snake
        """
        
        index = 0
        minhc = self.__game.getAbsDifAttacks(self.__tree[0]) + self.__tree[0].getCost()
        for i in range (1,len(self.__tree)):
            curr_hc = self.__game.getAbsDifAttacks(self.__tree[i]) + self.__tree[i].getCost()
            if( curr_hc <= minhc):
                index = i
                minhc = curr_hc

        curr_snake = self.__tree[index]            
        self.__tree = np.delete(self.__tree,index)

        return curr_snake


