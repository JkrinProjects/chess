BOARD_LENGTH = 8

from pieces import Piece, Pawn


def move(board):
    prev_square = board.grid[1][0]
    new_square = board.grid[2][0]
    temp = prev_square

    board.grid[1][0] = new_square
    board.grid[2][0] = temp
    return board

def column_letter_to_number(letter):
    base = ord("a")
    return(ord(letter)-base)

#function to validate input and convert chess notation to board.grid location (square A6 -> position (6,0))
def convert_chess_square_to_grid(square):
    if len(square) != 2:
        return ValueError("That is not a valid square")

    board_square = list(square)
    input_column = board_square[0].lower()
    input_row = board_square[1]

    if input_column < "a" or input_column > "h":
        return ValueError("Invalid Column")

    if input_row < "1" or input_row > "8":
        return ValueError("Invalid Row")

    grid_column = column_letter_to_number(input_column)
    grid_row = BOARD_LENGTH - int(input_row)

    return grid_row, grid_column



def move(board, starting_square_name, ending_square_name):

    #map the square name to the table position
    starting_row, starting_col = convert_chess_square_to_grid(starting_square_name)
    ending_row, ending_col = convert_chess_square_to_grid(ending_square_name)
    
    
    #get the piece at the grid location
    start_square_piece: Piece = board.grid[starting_row][starting_col] #the piece in this positin
    end_square_piece: Piece = board.grid[ending_row][ending_col] #should be empty or a capturable piece, can use its emptiness to verify valid move

    #check if the movement is valid
    if start_square_piece.is_valid_piece_movement()


    #Move the piece
    board.grid[starting_row][starting_col] = end_square_piece
    board.grid[ending_row][ending_col] = start_square_piece

    ###Older code
    #starting_row = BOARD_LENGTH - int(starting_board_square[1])
    #starting_col = column_letter_to_number(starting_board_square[0])
    

    #ending_row = BOARD_LENGTH - int(ending_square_name[1]) 
    #ending_col = column_letter_to_number(ending_board_square[0])
