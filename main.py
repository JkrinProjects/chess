from board import Board
from gamelogic import attempt_requested_move, get_chess_square



def main():

    game_board = Board()
    game_board.print_board()
    
    while True:
        #request starting square coordinates from the user and pass to get_chess_square to
        #validate the input and return a row and column 
        
        starting_row, starting_column = get_chess_square("Starting Position: (or quit): ")
        if starting_row is None:
            break

        ending_row, ending_column = get_chess_square("Ending Position: (or quit): ")
        if ending_row is None:
            break

        try:
            attempt_requested_move(game_board, starting_row, starting_column, ending_row, ending_column)
            game_board.print_board()
        except ValueError as error:
            print(error)
        


    
if __name__ == "__main__":
    main()