from pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King

BOARD_LENGTH = 8

class Board:

    def __init__(self):
        self.current_turn_color = "w"
        self.grid =  [
        [Rook("black"),Knight("black"),Bishop("black"),Queen("black"),King("black"),Bishop("black"),Knight("black"),Rook("black")],
        [Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black"),Pawn("black")],

        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None], 

        [Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white")],
        [Rook("white"),Knight("white"),Bishop("white"),Queen("white"),King("white"),Bishop("white"),Knight("white"),Rook("white")]
        ]

    def get_piece_location_and_color(self, piece, color):
        for row in range(BOARD_LENGTH):
            for column in range(BOARD_LENGTH):
                pass

    def change_turn(self):
        if self.current_turn_color == "white":
            self.current_turn_color = "black"
        else:
            self.current_turn_color = "white"



    def print_board(self):
        print(" ")
        print(" ".join(["a","b","c","d","e","f","g","h"]))
        for _ in range(16):
            print("-", end="")
        print(" ")
        for row in self.grid:
            new_row = []
            for piece in row:
                if piece is None:
                    new_row.append(".")
                else:
                    new_row.append(str(piece))
            print(" ".join(new_row))

        for _ in range(16):
            print("-", end="")
        print()
        print(" ".join(["a","b","c","d","e","f","g","h"]))
        print(" ")