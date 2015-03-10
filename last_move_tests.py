import unittest
from ChessBoard import ChessBoard


class LastMoveTests(unittest.TestCase):

    def setUp(self):
        self.cb = ChessBoard()

    def test_last_text_move_e2e4(self):
        self.cb.add_text_move('e2e4')
        assert self.cb.get_last_text_move() == "e4"

    def test_last_text_move_e2e4_f7f5(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        assert self.cb.get_last_text_move() == "f5"

