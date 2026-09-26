from board import Board
from gamelogic import move, is_valid_move

class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn_color = "white"

    def change_turn(self):
        if self.current_turn_color == "white":
            self.current_turn_color = "black"
        else:
            self.current_turn_color = "white"

    #performs the piece movement and returns two variables. A boolean for success/failure and either a string with an error message, or None
    def attempt_requested_move(board, starting_row, starting_col, ending_row, ending_col):

        #validated is the boolean which stores the boolean returned from is_valid_move()
        validated, error = is_valid_move(board, starting_row, starting_col, ending_row, ending_col)
        if not validated:
            return False, error

        move(board, starting_row, starting_col, ending_row, ending_col)

        return True, None
