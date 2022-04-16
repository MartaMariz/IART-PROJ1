from enum import Enum
class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    QUIT = 5
    BFS = 6
    ASTAR = 7
    MENU = 8
    START = 9
    SHOW = 10
    LOST = 11

class ALGORITHM(Enum):
    BFS = 1
    DFS = 2
    US = 4
    GS = 5
    As1 = 6
    As2 = 7
