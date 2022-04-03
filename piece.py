
class Piece:
    __col = 0
    __line = 0
    __totcol = 0
    __totline = 0
    __attack = []
    
    def __init__(self, col, line, totcol, totline):
        self.__col = col
        self.__line = line
        self.__totcol = totcol
        self.__totline = totline

    def getPos(self):
        return [self.__line,self.__col]
    
    def getAttack(self):
        return self.__attack
    


class Tower(Piece):
    def __init__(self, col, line, totcol, totline):
        super().__init__(self, col, line, totcol, totline)
        for i in range(self.__totline):
            self.__attack.push_back((i, self.__col)) 

        for i in range(self.__totcol):
            self.__attack.push_back((self.__line, i)) 



class Bishop(Piece):
    def __init__(self, col, line, totcol, totline):
        super().__init__(self, col, line, totcol, totline)




