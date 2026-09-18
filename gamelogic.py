BOARD_LENGTH = 8

from pieces import Piece


def column_letter_to_number(letter):
    base = ord("a")
    return(ord(letter)-base)

def get_chess_square(user_input):
    while True:
        input_square_name = input(user_input)
        
        if input_square_name.lower() == "quit":
            return None, None
        
        try:
            return convert_chess_square_to_grid(input_square_name)
        except ValueError as error:
            print(f"{error}: try again")
        

#function to validate input and convert chess notation to board.grid location (square A6 -> position (6,0))
def convert_chess_square_to_grid(square):
    if len(square) != 2:
        raise ValueError(f"{square} is not a valid square")

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

#check that the requested move is allowed by the selected piece's movement rules 
def movement_matches_piece_movement(board, starting_row, starting_col, ending_row, ending_col):
    moving_piece: Piece = board.grid[starting_row][starting_col] #the piece in this position
    #destination_of_moving_piece: Piece = board.grid[ending_row][ending_col] #should be empty or a capturable piece

    row_difference = ending_row - starting_row
    column_difference = ending_col - starting_col

    return moving_piece.is_valid_piece_movement(row_difference, column_difference)



#check that the end destination of the moving piece is not blocked.
def path_is_clear(board, starting_row, starting_col, ending_row, ending_col):

    if ending_row > starting_row:
        row_step = 1
    elif ending_row < starting_row:
        row_step = -1
    else:
        row_step = 0

    if ending_col > starting_col:
        column_step = 1
    elif ending_col < starting_col:
        column_step = -1
    else:
        column_step = 0

    current_row = starting_row + row_step
    current_column = starting_col + column_step

    while(current_row, current_column) != (ending_row, ending_col):
        if(board.grid[current_row][current_column] is not None):
            return False

        current_row += row_step
        current_column += column_step

    return True

#starting square has a piece
def starting_square_has_a_piece(board, starting_row, starting_col):
    return board.grid[starting_row][starting_col] is not None

#check that the square being moved to is empty or capturable,(the check to ensure the square is on the board is done when validating user input in get_chess_square() via convert_chess_square_to_grid())
def destination_is_valid(board, starting_row, starting_col, ending_row, ending_col):

    moving_piece: Piece = board.grid[starting_row][starting_col]
    destination_of_moving_piece: Piece = board.grid[ending_row][ending_col]

    #check for empty square as None has no attribute for color. If the destination square is not empty ensure it is the opposite color of the moving piece, allowing a capture
    if ((destination_of_moving_piece is None) or (destination_of_moving_piece.color != moving_piece.color)):
        return True

    return False
    
    
#function to aggregate all check/validation funcitons of piece movement
#returns a boolean representing a valid move and adds an error message if not
def is_valid_move(board, starting_row, starting_col, ending_row, ending_col):

    if not starting_square_has_a_piece(board, starting_row, starting_col):
        error = "There is no piece on starting square"
        return False, error

    #requested movement matches the movement rules of the piece at board[start_row][start_col]
    if not movement_matches_piece_movement(board, starting_row, starting_col, ending_row, ending_col):
        error = "that piece doesnt move that way"
        return False, error

    #path is not blocked
    if not path_is_clear(board, starting_row, starting_col, ending_row, ending_col):
        error = "the path to destination is blocked"
        return False, error

    #destination is either empty of an opposite color piece
    if not destination_is_valid(board, starting_row, starting_col, ending_row, ending_col):
        error = "that square is occupied by one of your pieces"
        return False, error

    return True, None

#move piece
def move(board, starting_row, starting_col, ending_row, ending_col):
    moving_piece: Piece = board.grid[starting_row][starting_col]
    #destination_of_moving_piece: Piece = board.grid[ending_row][ending_col] not needed, value of starting square has to be None after movement

    board.grid[ending_row][ending_col] = moving_piece
    board.grid[starting_row][starting_col] = None

#performs the piece movement and returns two variables. A boolean for success/failure and either a string with an error message, or None
def attempt_requested_move(board, starting_row, starting_col, ending_row, ending_col):

    #validated is the boolean which stores the boolean returned from is_valid_move()
    validated, error = is_valid_move(board, starting_row, starting_col, ending_row, ending_col)
    if not validated:
        return False, error
    
    move(board, starting_row, starting_col, ending_row, ending_col)

    return True, None


'''
#final function: converts input to chess notation, validates, and completes the move
def attempt_requested_move(board, starting_square_name, ending_square_name):

    #map the square name to the table position 
    starting_row, starting_col = convert_chess_square_to_grid(starting_square_name)
    ending_row, ending_col = convert_chess_square_to_grid(ending_square_name)

    if not is_valid_move(board, starting_row, starting_col, ending_row, ending_col):
        return False

    move(board, starting_row, starting_col, ending_row, ending_col)

    return True
'''


'''

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

    #check path to destination is not blocked


    ###Older code
    #starting_row = BOARD_LENGTH - int(starting_board_square[1])
    #starting_col = column_letter_to_number(starting_board_square[0])
    

    #ending_row = BOARD_LENGTH - int(ending_square_name[1]) 
    #ending_col = column_letter_to_number(ending_board_square[0])
'''
