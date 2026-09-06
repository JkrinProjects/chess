from pieces import Piece, Pawn

class Board:

    #replace "." with None in the future
    def __init__(self):
        self.grid =  [
        ["r","h","b","q","k","b","h","r"],
        [Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black")],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],    
        ["P","P","P","P","P","P","P","P"],
        ["R","H","B","Q","K","B","H","R"]
        ]

    def print_board(self):
        print(" ")
        print(" ".join(["a","b","c","d","e","f","g","h"]))
        for row in self.grid:
            print(" ".join(str(piece) for piece in row))
        print(" ")