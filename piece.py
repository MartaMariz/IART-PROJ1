
class Piece:
    _col = 0
    _line = 0
    _totcol = 0
    _totline = 0
    _attack = []
    
    def __init__(self, col, line, totcol, totline):
        self._col = col
        self._line = line
        self._totcol = totcol
        self._totline = totline

    def getPos(self):
        return [self._line,self._col]
    
    def getAttack(self):
        return self._attack
    
    def printAttack(self):
        for l in range (len(self._attack)):
                print( self._attack[l])
    


class Tower(Piece):
    def __init__(self, col, line, totcol, totline):
        super().__init__(col, line, totcol, totline)
        for i in range(self._totline):
            self._attack.append((i, self._col)) 

        for i in range(self._totcol):
            self._attack.append((self._line, i)) 



class Bishop(Piece):
    def __init__(self, col, line, totcol, totline):
        super().__init__(col, line, totcol, totline)
        xnyn = True
        xnyp = True
        xpyn = True
        xpyp = True
        i = 1
        while ( xnyn or xnyp or xpyn or xpyp) :
            if ( self._line - i >= 0 and self._col - i >= 0 and xnyn ):
                self._attack.append(( self._line - i,self._col - i ))
            else : xnyn = False
            if ( self._line + i < self._totline and self._col - i >= 0 and xnyp ):
                self._attack.append(( self._line + i,self._col - i ))
            else : xnyp = False
            if ( self._line - i >= 0 and self._col + i < self._totcol and xpyn ):
                self._attack.append(( self._line - i,self._col + i ))
            else : xpyn = False 
            if ( self._line + i < self._totline and self._col + i < self._totcol and xpyp ):
                self._attack.append(( self._line + i,self._col + i ))
            else : xpyp = False 
            i += 1








