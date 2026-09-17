BOARD_LENGTH = 8

from pieces import Piece, Pawn


def column_letter_to_number(letter):
    base = ord("a")
    return(ord(letter)-base)

#function to validate input and convert chess notation to board.grid location (square A6 -> position (6,0))
def convert_chess_square_to_grid(square):
    if len(square) != 2:
        raise ValueError("That is not a valid square")

    board_square = list(square)
    input_column = board_square[0].lower()
    input_row = board_square[1]

    if input_column < "a" or input_column > "h":
        raise ValueError("Invalid Column")

    if input_row < "1" or input_row > "8":
        raise ValueError("Invalid Row")

    grid_column = column_letter_to_number(input_column)
    grid_row = BOARD_LENGTH - int(input_row)

    return grid_row, grid_column



def move(board, starting_square_name, ending_square_name):

    #map the square name to the table position
    starting_row, starting_col = convert_chess_square_to_grid(starting_square_name)
    ending_row, ending_col = convert_chess_square_to_grid(ending_square_name)

    row_difference = ending_row - starting_row
    column_difference = ending_col - starting_col
    
    #get the piece at the grid location
    moving_piece: Piece = board.grid[starting_row][starting_col] #the piece in this positin
    destination_of_moving_piece: Piece = board.grid[ending_row][ending_col] #should be empty or a capturable piece, can use its emptiness to verify valid move

    #check if the movement is valid
    if moving_piece.is_valid_piece_movement(row_difference, column_difference):
        #Move the piece
        board.grid[starting_row][starting_col] = destination_of_moving_piece
        board.grid[ending_row][ending_col] = moving_piece

        return True
    return False

    ###Older code
    #starting_row = BOARD_LENGTH - int(starting_board_square[1])
    #starting_col = column_letter_to_number(starting_board_square[0])
    

    #ending_row = BOARD_LENGTH - int(ending_square_name[1]) 
    #ending_col = column_letter_to_number(ending_board_square[0])
