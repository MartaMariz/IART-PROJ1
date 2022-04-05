from piece import Bishop, Piece, Tower, Queen, Horse

board = [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, Queen(2, 2, 5, 5), None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
        ]

if (board[2][2] is not None):
    board[2][2].printAttack()