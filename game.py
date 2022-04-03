from piece import Piece

board = [[None, Piece(1,0)],
        [Piece(0,1), None]]

if (board[0][1] is not None):
    print(board[0][1].getPos()[0])
