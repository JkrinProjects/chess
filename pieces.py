from abc import ABC, abstractmethod
from gamelogic import convert_chess_square_to_grid

class Piece(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def is_valid_piece_movement(self, starting_square, ending_square):
        pass

    @abstractmethod
    def is_valid_capture_movement(self, starting_square, ending_square):
        pass




class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)

    def is_valid_piece_movement(self, starting_square, ending_square):

        #get table coordinates from chess notation
        starting_row, starting_col = convert_chess_square_to_grid(starting_square)
        ending_row, ending_col = convert_chess_square_to_grid(ending_square) #perhaps def func to do start & end at same time

        #get difference in row and column
        row_difference = ending_row - starting_row
        column_difference = ending_col - starting_col

        #define piece movement by checking if difference of row & column are correct
        if ((row_difference > 1 or row_difference < 0) and (column_difference == 0)):
            return row_difference

    def is_valid_capture_movement(self, starting_square, ending_square):
        pass
    

class Rook(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

