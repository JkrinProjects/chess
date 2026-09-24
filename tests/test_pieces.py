#https://docs.python.org/3/library/unittest.html
#self note - subtest will finish all test cases and distingish the failed cases

import unittest

from pieces import Pawn, Rook, Bishop, Knight, Queen, King

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


#example subtest
'''class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)'''

'''    #single instances of movement tests
    def test_knight_correctly_moves_two_row_one_column(self):
        self.assertTrue(self.knight.is_valid_piece_movement(2,1))

    def test_knight_correctly_moves_two_columns_one_row(self):
        self.assertTrue(self.knight.is_valid_piece_movement(1,2))

    def test_knight_doesnt_move_straight_line(self):
        self.assertFalse(self.knight.is_valid_piece_movement(2,0))

    def test_knight_doesnt_move_diagonal(self):
        self.assertFalse(self.knight.is_valid_piece_movement(1,1))

    def test_knight_doesnt_move_more_than_two_rows(self):
        self.assertFalse(self.knight.is_valid_piece_movement(3,1))

    def test_knight_doesnt_move_more_than_two_columns(self):
        self.assertFalse(self.knight.is_valid_piece_movement(1,3))'''
    

