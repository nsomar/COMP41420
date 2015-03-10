import unittest
from ChessBoard import ChessBoard


class CagriTests(unittest.TestCase):

    def setUp(self):
        self.cb = ChessBoard()

    def test_game_not_over(self):
        assert not self.cb._game_result

    def test_invalid_from_location(self):
        assert not self.cb.add_move((-1, 0), (2, 4))

    def test_invalid_to_location(self):
        assert not self.cb.add_move((3, 5), (-1, 6))

    def test_if_different_from_and_to(self):
        assert not self.cb.add_move((6, 2), (6, 2))

    # At the start of the game the board is at its initial state
    # Hence, it returns true for the check at (4,2) and false on others
    def test_if_target_free(self):
        assert self.cb.is_free(4, 2)
        assert not self.cb.is_free(1, 1)
        assert not self.cb.is_free(7, 7)

    # At the initial state of the game turn is on the WHITE player
    # 7,7 belongs to the WHITE so it returns true while 1,1 belongs to
    # BLACK and returns false
    def test_if_piece_correct_color(self):
        assert not (self.cb.get_color(1, 1) == self.cb._turn)
        assert (self.cb.get_color(7, 7) == self.cb._turn)

    # This should be false at the beginning as its an ending condition
    def test_if_fifty_rule_matches(self):
        assert not (self.cb._fifty == 100)

    # This should be false at the beginning as its an ending condition
    def test_three_repetitions(self):
        assert not self.cb.three_repetitions()

    # Testing movement of a white pawn from c2 to c3
    def test_move_pawn(self):
        assert self.cb.add_move((2, 6), (2, 5))

    # To test the rook movement, first the blocking pawn must be moved
    # After moving the blocking pawn, a black pawn must be moved to be
    # able to move the rook.
    def test_move_rook(self):
        self.cb.add_move((0, 6), (0, 5))
        self.cb.add_move((6, 1), (6, 2))
        assert self.cb.add_move((0, 7), (0, 6))

    # To test the bishop movement, first the blocking pawn must be moved
    # After moving the blocking pawn on the top left corner,
    # a black pawn must be moved to be able to move the bishop.
    def test_move_bishop(self):
        self.cb.add_move((1, 6), (1, 5))
        self.cb.add_move((6, 1), (6, 2))
        assert self.cb.add_move((2, 7), (1, 6))

    # def test_move_queen(self):
    # def test_move_king(self):
    # def test_move_knight(self):
