from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color):
        self.color = color
        self.letter = None

    #print function
    def __str__(self):
        return f"{self.color}: {self.letter}"
    
    @abstractmethod
    def is_valid_piece_movement(self, row_difference, column_difference):
        pass

class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.letter = "P"

    def is_valid_piece_movement(self, row_difference, column_difference):

        #black pawns only move +1 row, white pawns only move -1 row

        #black pawn moveme
        if self.color == "black":

            #move down the board
            if(column_difference == 0 and row_difference == 1):
                return True
            #capture down
            if ((column_difference == 1 or column_difference == -1) and row_difference == 1):
                return True
            
        #white pawn movement
        if self.color == "white":   
            #move up the board
            if(column_difference == 0 and row_difference == -1):
                return True
            #capture up
            if ((column_difference == 1 or column_difference == -1) and row_difference == -1):
                return True
        return False

    

class Rook(Piece):
     
    def is_valid_piece_movement(self, row_difference, column_difference):
        if (row_difference == 0 and column_difference != 0):
            return True
        if (row_difference != 0 and column_difference == 0):
            return True
        return False


class Knight(Piece):

    def is_valid_piece_movement(self, row_difference, column_difference):
            if (abs(row_difference) == 2 and abs(column_difference) == 1):
                return True
            if (abs(row_difference) == 1 and abs(column_difference) == 2):
                return True
    pass

class Bishop(Piece):

    def is_valid_piece_movement(self, row_difference, column_difference):
        if(row_difference == 0 or column_difference == 0):
            return False

        if(abs(row_difference)==abs(column_difference)):
            return True
    

class Queen(Piece):
    
    def is_valid_piece_movement(self, row_difference, column_difference):
        if (row_difference == 0 and column_difference != 0):
            return True
        if (row_difference != 0 and column_difference == 0):
            return True
        if(abs(row_difference) == abs(column_difference)):
            return True

    

class King(Piece):
    pass



'''       
    def get_row_and_column_difference(self, starting_row, ending_square):
        #get table coordinates from chess notation
        starting_row, starting_col = convert_chess_square_to_grid(starting_square)
        ending_row, ending_col = convert_chess_square_to_grid(ending_square)

        #find difference
        row_difference = ending_row - starting_row
        column_difference = ending_col - starting_col

        return row_difference, column_difference        

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