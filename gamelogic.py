BOARD_LENGTH = 8

from pieces import Piece, Pawn, Knight, King, Queen, Bishop, Rook


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



#check that the end destination of the moving piece is not blocked. Knights can jump so are not concerned with clear path
def path_is_clear(board, starting_row, starting_col, ending_row, ending_col):

    moving_piece = board.grid[starting_row][starting_row]
    if isinstance(moving_piece, Knight):
        return True

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

    #Special rules for Pawn capture & first move    
    #pawn only has diagonal captures, can travel two spaces traveled on first move, and can turn into any piece on promotion(reaching the oppponents back rank)
    if isinstance(moving_piece, Pawn):
        if abs(ending_col - starting_col) == 1: #column difference can only be 1 on a capture
            return((destination_of_moving_piece is not None) and (destination_of_moving_piece.color != moving_piece.color))


    #check for empty square. If the destination square is not empty ensure it is the opposite color of the moving piece, allowing a capture
    #need a special case/check for pawns(cant capture straight)
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


#pawn promotion
#function to check a pawn made it to the opponent's back rank
def pawn_can_promote(board, piece, row, column):

    if not isinstance(piece, Pawn):
        return False

    if ((piece.color == "white") and (row == 0)):
        return True
    if ((piece.color == "black") and (row == 7)):
        return True

    return False

#function to promote the pawn. replaces the Pawn instance with a newly instantiated Piece.(defaults to Queen for now)
def promote_pawn(board, piece, row, column):
    if (piece.color == "white"):
        board.grid[row][column] = Queen("white")

    if (piece.color == "black"):
        board.grid[row][column] = Queen("black")
    

#move piece
def move(board, starting_row, starting_col, ending_row, ending_col):
    moving_piece: Piece = board.grid[starting_row][starting_col]
    #destination_of_moving_piece: Piece = board.grid[ending_row][ending_col] not needed, value of starting square has to be None after movement

    board.grid[ending_row][ending_col] = moving_piece
    board.grid[starting_row][starting_col] = None

    moving_piece.hasmoved = True

    if(pawn_can_promote(board, moving_piece, ending_row, ending_col)):
        promote_pawn(board, moving_piece, ending_row, ending_col)

#performs the piece movement and returns two variables. A boolean for success/failure and either a string with an error message, or None
def attempt_requested_move(board, starting_row, starting_col, ending_row, ending_col):

    #validated is the boolean which stores the boolean returned from is_valid_move()
    validated, error = is_valid_move(board, starting_row, starting_col, ending_row, ending_col)
    if not validated:
        return False, error
    
    move(board, starting_row, starting_col, ending_row, ending_col)

    return True, None