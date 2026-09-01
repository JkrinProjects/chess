from board import Board
from gamelogic import move



def main():

    game_board = Board()
    game_board.print_board()

    while True:
        start_position = input("Starting Position: ")
        end_position = input("Ending Position: ")
        move(game_board, start_position, end_position)
        game_board.print_board()

    
if __name__ == "__main__":
    main()