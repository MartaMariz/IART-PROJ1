from piece import Bishop, Piece, Tower

board = [
        [None, Piece( 1, 0, 4, 4), None, None],
        [None, None, None, None],
        [None, None,Bishop(2, 2, 4, 4), None],
        [None, None, None, None]
        ]

if (board[2][2] is not None):
    board[2][2].printAttack()