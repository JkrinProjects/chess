BOARD_LENGTH = 8


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

def move(board, starting_square_name, ending_square_name):

    #create a list of the square name to parse the col/row
    starting_board_square = list(starting_square_name)
    ending_board_square = list(ending_square_name)

    #map the square name to the table position, square A6 -> position (0,2)
    starting_row = BOARD_LENGTH % int(starting_board_square[1])
    starting_col = column_letter_to_number(starting_board_square[0])
    start_square_piece = board.grid[starting_row][starting_col] #the piece in this positin

    ending_row = BOARD_LENGTH % int(ending_square_name[1]) 
    ending_col = column_letter_to_number(ending_board_square[0])
    end_square_piece = board.grid[ending_row][ending_col] #should be empty, can use its emptiness to verify valid move


    #Move the piece
    board.grid[starting_row][starting_col] = end_square_piece
    board.grid[ending_row][ending_col] = start_square_piece
