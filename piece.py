
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

    def diagonalAttack(self):
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

    def perpendicularAttack(self):
        for i in range(self._totline):
            if (i != self._line):
                self._attack.append((i, self._col)) 

        for i in range(self._totcol):
            if (i != self._col):
                self._attack.append((self._line, i)) 
    


class Tower(Piece):
    def __init__(self, col, line, totcol, totline):
        super().__init__(col, line, totcol, totline)
        super().perpendicularAttack()



class Bishop(Piece):
    def __init__(self, col, line, totcol, totline):
        super().__init__(col, line, totcol, totline)
        super().diagonalAttack()
        

class Queen(Piece):
    def __init__(self, col, line, totcol, totline):
        super().__init__(col, line, totcol, totline)
        super().diagonalAttack()
        super().perpendicularAttack()



class Horse(Piece):
    def __init__(self, col, line, totcol, totline):
        super().__init__(col, line, totcol, totline)

        l = self._line
        c = self._col
        if (l > 0):
            l -= 1
            if (l >= 0):
                if (c >= 2):
                    self._attack.append((l, c-2))
                if (c <= totcol-3):
                    self._attack.append((l, c+2))
            if (l > 0):
                l -= 1
                if (c >= 1):
                    self._attack.append((l, c-1))
                if (c <= totcol-2):
                    self._attack.append((l, c+1))

        l = self._line
        if (l < totline-1):
            l += 1
            if (l <= totline-1):
                if (c >= 2):
                    self._attack.append((l, c-2))
                if (c <= totcol-3):
                    self._attack.append((l, c+2))
            if (l < totline-1):
                l += 1
                if (c >= 1):
                    self._attack.append((l, c-1))
                if (c <= totcol-2):
                    self._attack.append((l, c+1))

        l = self._line
        if (c > 0):
            c -= 1
            if (c >= 0):
                if (l >= 2):
                    self._attack.append((l-2, c))
                if (l <= totline-3):
                    self._attack.append((l+2, c))
            if (c > 0):
                c -= 1
                if (l >= 1):
                    self._attack.append((l-1, c))
                if (l <= totline-2):
                    self._attack.append((l+1, c))

        c = self._col
        if (c < totcol-1):
            c += 1
            if (c <= totcol-1):
                if (l >= 2):
                    self._attack.append((l-2, c))
                if (l <= totline-3):
                    self._attack.append((l+2, c))
            if (c < totcol-1):
                c += 1
                if (l >= 1):
                    self._attack.append((l-1, c))
                if (l <= totline-2):
                    self._attack.append((l+1, c))


