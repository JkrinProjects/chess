import unittest

from gamelogic import is_valid_move, attempt_requested_move, pawn_can_promote
from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from board import Board

class TestPawnCapture(unittest.TestCase):
    def test_black_pawn_capture_white_piece(self):
        board = Board()
        black_pawn = Pawn("black")

        white_pawn = Pawn("white")
        white_bishop = Bishop("white")
        white_knight = Knight("white")
        white_rook = Rook("white")
        white_queen = Queen("white")
        white_pieces_population = [white_pawn, white_bishop, white_knight, white_rook, white_queen]

        board.grid[3][3] = black_pawn
        for piece in white_pieces_population:
            with self.subTest(piece = piece):
                board.grid[4][4] = piece #assign the piece to a capturable square
                self.assertTrue(attempt_requested_move(board,3,3,4,4))
                board.grid[3][3] = black_pawn

    def test_black_pawn_doesnt_capture_black_piece(self):
        board = Board()

        black_pawn = Pawn("black")
        black_bishop = Bishop("black")
        black_knight = Knight("black")
        black_rook = Rook("black")
        black_queen = Queen("black")
        black_pieces_population = [black_pawn, black_bishop, black_knight, black_rook, black_queen]

        board.grid[3][3] = black_pawn
        for piece in black_pieces_population:
            with self.subTest(piece = piece):
                board.grid[4][4] = piece #assign the piece to a capturable square
                self.assertFalse(attempt_requested_move(board,3,3,4,4))
                board.grid[3][3] = black_pawn
    
    def test_white_pawn_capture_black_piece(self):
        board = Board()
        white_pawn = Pawn("white")
        
        black_pawn = Pawn("black")
        black_bishop = Bishop("black")
        black_knight = Knight("black")
        black_rook = Rook("black")
        black_queen = Queen("black")
        black_pieces_population = [black_pawn, black_bishop, black_knight, black_rook, black_queen]

        board.grid[3][3] = white_pawn
        for piece in black_pieces_population:
            with self.subTest(piece = piece):
                board.grid[4][4] = piece #assign the piece to a capturable square
                self.assertTrue(attempt_requested_move(board,4,4,3,3))
                board.grid[3][3] = white_pawn
    
    def test_black_pawn_doesnt_capture_black_piece(self):
        board = Board()
        
        white_pawn = Pawn("white")
        white_bishop = Bishop("white")
        white_knight = Knight("white")
        white_rook = Rook("white")
        white_queen = Queen("white")
        white_pieces_population = [white_pawn, white_bishop, white_knight, white_rook, white_queen]

        board.grid[3][3] = white_pawn
        for piece in white_pieces_population:
            with self.subTest(piece = piece):
                board.grid[4][4] = piece #assign the piece to a capturable square
                self.assertTrue(attempt_requested_move(board,4,4,3,3))
                board.grid[3][3] = white_pawn

class TestPawnPromotion(unittest.TestCase):
    def test_pawn_is_on_correct_row_to_promote(self):
        white_pawn = Pawn("white")
        black_pawn = Pawn("black")
        board = Board()
        test_cases_for_promotion = [(white_pawn,0),(black_pawn,7)]
        
        for pawn, row in test_cases_for_promotion:
                with self.subTest(color=pawn.color, promotion_row=row):
                    self.assertTrue(pawn_can_promote(board, pawn, row,0)) 

    def test_pawn_doesnt_promote_on_wrong_row(self):
        white_pawn = Pawn("white")
        black_pawn = Pawn("black")
        board = Board()
        test_cases_for_promotion = [(white_pawn,0),(black_pawn,7)]

        for pawn, row in test_cases_for_promotion:
            for row in range(1,7):
                with self.subTest(color=pawn.color, row=row):
                    self.assertFalse(pawn_can_promote(board, pawn, row, 0))

    def test_black_pawn_promotion_success(self):
        board = Board()
        black_pawn = Pawn("black")

        board.grid[6][0] = black_pawn
        #attempt_requested_move() returns a boolean and an error message
        successful_promotion, error = attempt_requested_move(board, 6,0,7,0) #move from second to last row to white back rank

        #test returned value
        self.assertTrue(successful_promotion)
        self.assertIsNone(error)

        #test new piece object replaced pawn on board
        self.assertIsInstance(board.grid[7][0], Queen)
        
        empty_square = board.grid[6][0]
        self.assertIsNone(empty_square)

        new_pieces_color = board.grid[7][0].color
        self.assertEqual("black", new_pieces_color)

    def test_white_pawn_promotion_success(self):
        board = Board()
        pawn = Pawn("white")

        board.grid[1][0] = pawn
        #attempt_requested_move() returns a boolean and an error message
        successful_promotion, error = attempt_requested_move(board,1,0,0,0) #move from second to last row to white back rank

        #test returned value
        self.assertTrue(successful_promotion)
        self.assertIsNone(error)

        #test new piece object replaced pawn on board
        self.assertIsInstance(board.grid[0][0], Queen)
        
        empty_square = board.grid[1][0]
        self.assertIsNone(empty_square)

        new_pieces_color = board.grid[0][0].color
        self.assertEqual("white", new_pieces_color)
        