#https://docs.python.org/3/library/unittest.html
#self note - subtest will finish all test cases and distingish the failed cases

import unittest

from pieces import Pawn, Rook, Bishop, Knight, Queen, King
from board import Board

#knight movement
class TestKnightMovement(unittest.TestCase):
    knight = Knight("white")

    #subtest method
    def test_valid_knight_move_population(self):
        valid_moves = [(2,1),(2,-1),(-2,1),(-2,-1),
                        (1,2),(1,-2),(-1,2),(-1,-2)]

        for row_difference, column_difference in valid_moves:
            with self.subTest(row_difference = row_difference, column_difference = column_difference):
                self.assertTrue(self.knight.is_valid_piece_movement(row_difference, column_difference))

    def test_invalid_knight_move_population(self):
        non_valid_moves = [("no movement",0,0),("too many rows",3,1),("too many columns",1,3),
                       ("positive diagonal one",1,1),("negative diagonal one",-1,-1),("positive diagonal two",2,2),("negative diagonal two",-2,-2),
                       ("vertical one",1,0),("vertical two",2,0),("horizontal one",0,1),("horizontal two",0,2)]

        for movement_type, row_difference, column_difference in non_valid_moves:
            with self.subTest(movement_type = movement_type):
                self.assertFalse(self.knight.is_valid_piece_movement(row_difference, column_difference))
#example subtest below


class TestPawnMovement(unittest.TestCase):
    capture_direction = [("right", 1 ),("left", -1)]
    
    #white moves
    def test_white_pawn_moves_forward(self):
        pawn = Pawn("white")
        self.assertTrue(pawn.is_valid_piece_movement(-1,0))

    def test_white_pawn_doesnt_move_backward(self):
        pawn = Pawn("white")
        self.assertFalse(pawn.is_valid_piece_movement(1,0))

    def test_white_can_travel_two_spaces_from_starting_square(self):
        pawn = Pawn("white")
        pawn.hasmoved = False
        self.assertTrue(pawn.is_valid_piece_movement(-2,0))        

    def test_white_cant_travel_two_after_moving(self):
        pawn = Pawn("white")
        pawn.hasmoved = True
        self.assertFalse(pawn.is_valid_piece_movement(-2,0))

    def test_white_cant_travel_two_after_moving(self):
        pawn = Pawn("white")
        pawn.hasmoved = True
        self.assertFalse(pawn.is_valid_piece_movement(-2,0))

    #test to ensure that a pawn is allowed to move diagnally 1 column per its rules
    def test_white_can_move_diagonal_where_applicable(self):
        pawn_has_moved_before = Pawn("white")
        pawn_has_moved_before.hasmoved = True

        pawn_has_not_moved_before = Pawn("white")
        pawn_has_not_moved_before.hasmoved = False

        pawn_test_captures = [pawn_has_moved_before, pawn_has_not_moved_before]
        for pawn in pawn_test_captures:
            for direction, column_difference in self.capture_direction:
                with self.subTest(has_moved_before=pawn.hasmoved, column_difference=direction):
                    self.assertTrue(pawn.is_valid_piece_movement(-1,column_difference))


    #black  moves
    def test_black_pawn_moves_forward(self):
        pawn = Pawn("black")
        self.assertTrue(pawn.is_valid_piece_movement(1,0))

    def test_black_pawn_doesnt_move_backward(self):
        pawn = Pawn("black")
        self.assertFalse(pawn.is_valid_piece_movement(-1,0))
    
    def test_black_can_travel_two_spaces_from_starting_square(self):
        pawn = Pawn("black")
        pawn.hasmoved = False
        self.assertTrue(pawn.is_valid_piece_movement(2,0))   
    
    def test_black_cant_capture_two_square_before_has_moved(self):
        pawn = Pawn("black")
        pawn.hasmoved = False
        for direction, column_difference in self.capture_direction:
            with self.subTest(column_difference = column_difference):
                self.assertFalse(pawn.is_valid_piece_movement(2,1))

    def test_black_cant_travel_two_after_moving(self):
        pawn = Pawn("black")
        pawn.hasmoved = True
        self.assertFalse(pawn.is_valid_piece_movement(2,0))

    #test to ensure that a pawn is allowed to move diagnally 1 column per its rules
    def test_black_can_move_diagonal_where_applicable(self):
        pawn_has_moved_before = Pawn("black")
        pawn_has_moved_before.hasmoved = True

        pawn_has_not_moved_before = Pawn("black")
        pawn_has_not_moved_before.hasmoved = False

        pawn_test_captures = [pawn_has_moved_before, pawn_has_not_moved_before]
        for pawn in pawn_test_captures:
            for direction, column_difference in self.capture_direction:
                with self.subTest(has_moved_before=pawn.hasmoved, column_difference=direction):
                    self.assertTrue(pawn.is_valid_piece_movement(1,column_difference))




    
##example for reference
'''class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)'''






