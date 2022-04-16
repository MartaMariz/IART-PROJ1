from enum import Enum
class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    QUIT = 5
    MENU = 6
    START = 7
    SHOWE = 8
    LOST = 9
    BFS = 10
    UCOST = 11
    GS1 = 12
    GS2 = 13
    AS1 = 14
    AS2 = 15
    RULES = 16
    SHOWH = 17

class ALGORITHM(Enum):
    BFS = 1
    DFS = 2
    UCOST = 4
    GS1 = 5
    As1 = 6
    As2 = 7
