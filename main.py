from board import Board
from gamelogic import move



def main():

    game_board = Board()
    game_board.print_board()

    start_position = "a7"
    end_position = "a6"

    move(game_board, start_position, end_position)

    game_board.print_board()

    
if __name__ == "__main__":
    main()