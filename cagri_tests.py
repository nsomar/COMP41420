import unittest
from ChessBoard import ChessBoard


class MyChessBoard(ChessBoard):

    def add_move(self, from_pos, to_pos):
        self.called_from_pos = from_pos
        self.called_to_pos = to_pos


class CagriTests(unittest.TestCase):

    def setUp(self):
        self.cb = MyChessBoard()

    ######################################
    # Unittests for add_text_move method #
    ######################################

    # Check if the (0,0) and (0,7) is movable
    def test_a1_a8_movable(self):
        self.cb.add_text_move('a1a8')
        assert self.cb.called_from_pos == (0, 7)
        assert self.cb.called_to_pos == (0, 0)

    # Check if 'a0a9' is not movable (out of bounds)
    def test_a0_a9_not_movable(self):
        assert not self.cb.add_text_move('a0a9')

    # Check if 'a1a9' is not movable (out of bounds)
    def test_a1_a9_not_movable(self):
        assert not self.cb.add_text_move('a1a9')

    # Check if the (7,0) and (7,7) is movable
    def test_h1_h8_movable(self):
        self.cb.add_text_move('h1h8')
        assert self.cb.called_from_pos == (7, 7)
        assert self.cb.called_to_pos == (7, 0)

    # Check if 'h0h9' is not movable (out of bounds)
    def test_h0_h9_not_movable(self):
        assert not self.cb.add_text_move('h0h9')

    # Check if 'h1h9' is not movable (out of bounds)
    def test_h1_h9_not_movable(self):
        assert not self.cb.add_text_move('h1h9')

    # Checks if the caps lock commands are not working
    def test_caps_are_not_working(self):
        assert not self.cb.add_text_move('A3F5')

    # Checks if many moves are working
    # Accepts the last 2 commands
    def test_multiple_moves_working(self):
        self.cb.add_text_move('b7e3d2a5')
        assert self.cb.called_from_pos == (3, 6)
        assert self.cb.called_to_pos == (0, 3)

    # Tests below this line checks if the moves defined in the main are valid moves.
    def test_e2_e4_movable(self):
        self.cb.add_text_move('e2e4')
        assert self.cb.called_from_pos == (4, 6)
        assert self.cb.called_to_pos == (4, 4)

    def test_f7_f5_movable(self):
        self.cb.add_text_move('f7f5')
        assert self.cb.called_from_pos == (5, 1)
        assert self.cb.called_to_pos == (5, 3)

    def test_e4_f5_movable(self):
        self.cb.add_text_move('e4f5')
        assert self.cb.called_from_pos == (4, 4)
        assert self.cb.called_to_pos == (5, 3)

    def test_g8_h6_movable(self):
        self.cb.add_text_move('g8h6')
        assert self.cb.called_from_pos == (6, 0)
        assert self.cb.called_to_pos == (7, 2)

    def test_f1_d3_movable(self):
        self.cb.add_text_move('f1d3')
        assert self.cb.called_from_pos == (5, 7)
        assert self.cb.called_to_pos == (3, 5)

    def test_h6_f5_movable(self):
        self.cb.add_text_move('h6f5')
        assert self.cb.called_from_pos == (7, 2)
        assert self.cb.called_to_pos == (5, 3)

    def test_d3_f5_movable(self):
        self.cb.add_text_move('d3f5')
        assert self.cb.called_from_pos == (3, 5)
        assert self.cb.called_to_pos == (5, 3)