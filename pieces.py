from abc import ABC, abstractmethod
from gamelogic import convert_chess_square_to_grid







class Piece(ABC):
    def __init__(self, color):
        self.color = color
        self.letter = None

    def get_row_and_column_difference(self, starting_square, ending_square):
        #get table coordinates from chess notation
        starting_row, starting_col = convert_chess_square_to_grid(starting_square)
        ending_row, ending_col = convert_chess_square_to_grid(ending_square)

        #find difference
        row_difference = ending_row - starting_row
        column_difference = ending_col - starting_col

        return row_difference, column_difference

    #print function
    def __str__(self):
        return f"{self.color}: {self.letter}"
    
    @abstractmethod
    def is_valid_piece_movement(self, starting_square, ending_square):
        pass

class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.letter = "P"

    def is_valid_piece_movement(self, starting_square, ending_square):

        row_difference, column_difference = self.get_row_and_column_difference(starting_square, ending_square)

        #black pawns only move +1 row, white pawns only move -1 row

        #black pawn moveme
        if self.color == "black":
            if(column_difference == 0 and row_difference == 1)
                return True
            #capture
            if ((column_difference == 1 or column_difference == -1) and row_difference == 1):
                return True
        return False
            
                
        #white pawn movement
        if self.color == "white":
            if column_difference == 0:
                if row_difference == -1:
                    return True
                else:
                    return False

        #capture
        if column_difference == 1 or column_difference == -1:
            if row_difference == 1:
                return True
            else:
                return False


    

class Rook(Piece):
     
     def is_valid_piece_movement(self, starting_square, ending_square):
        row_difference, column_difference = self.get_row_and_column_difference(starting_square, ending_square)


class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass



'''       
        if self.color == "black":
            if column_difference == 0:
                if row_difference == 1:
                    return True
                else:
                    return False




#capture
        if column_difference == 1 or column_difference == -1:
            if row_difference == 1:
                return True
            else:
                return False'''